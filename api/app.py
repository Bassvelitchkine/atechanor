from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from dataBaseManager import DataBaseManager
from io import StringIO
from werkzeug.wrappers import Response
from rq import Queue
from rq.job import Job
from emailScraper import emailScraper
import redis
from flask_mail import Mail, Message
from flask_cors import CORS

# Database connection
dbManager = DataBaseManager('database/database.db', 'database/schemas.sql')
# Reddis and queue
conn = redis.from_url("redis://redis:6379")
q = Queue(connection=conn, default_timeout=1000)
# Flask app
app = Flask(__name__)
# CORS policies
cors = CORS(app)
# Flask mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bastien.velitchkine@gmail.com'
app.config['MAIL_PASSWORD'] = 'gymnastique'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/submit', methods=('POST',))
def submitRequest():
    """
    """
    if request.method == 'POST':
        email = request.json['email']
        profilesList = request.json['profilesList']

        if not (email or profilesList):
            if not email:
                flash('Email is required!')
            if not profilesList:
                flash("A list of profiles is required!")
        else:
            # Add initiator to database if his not in it
            dbManager.addInitiator(email)
            # Add profiles list to database
            profilesToScrape, nbProfilesToProcess = dbManager.addProfiles(
                profilesList)
            # Add request to database
            requestId = dbManager.addRequest(
                email, profilesList, nbProfilesToProcess)
            # Link request to requested profiles
            dbManager.connectRequestAndProfiles(requestId, profilesList)

            # Add tasks to the queue
            for profileUrl in profilesToScrape:
                job = q.enqueue_call(
                    func=emailScraper, args=(profileUrl,), result_ttl=5000)
                print("\n Job id: " + job.get_id() + "\n")

            return "OK"


@app.route('/update', methods=('PUT',))
def updateProfileEmail():
    """
    INPUT:
        - urlPortion (str): the part of the url that differenciates several stackoverflow users
        - email (str): the email found for the stackoverflow profile
    OUTPUT: 
        - None
    ****
    The function updates the profile email in the profiles table as well as the requests in the associated table to see
    if the request is ready.
    """
    profileUrl = request.json["profileUrl"]
    emails = ",".join(request.json["emails"])

    # Let's update first the profile whose email was eventually found
    dbManager.updateProfileEmail(profileUrl, emails)

    # Let's update requests that have said profile in their request
    initiatorStatisfied = dbManager.updateRequestStatus(profileUrl)

    # Send download link to initiators satisfied
    for initiator in initiatorStatisfied:
        msg = Message('Your export is ready',
                      sender='bastien.velitchkine@gmail.com', recipients=[initiator[0]])
        msg.body = "http://192.168.99.100:5000/download/" + \
            initiator[1]  # We add the download link
        mail.send(msg)

    return "ALL RIGHT"


@app.route('/download/<string:downloadLink>', methods=('GET',))
def download(downloadLink):
    """
    INPUT:
        - downloadLink (str): the hash associated to a particular request.
    OUTPUT:
        - csv
    ***
    The function generates a csv file to download from the list of profile urls and their requested emails.
    """
    import csv

    def generate(res):
        """
        Dynamically generates the csv file to download
        """
        data = StringIO()
        w = csv.writer(data)

        # write header
        w.writerow(('timestamp', 'stackoverflowURL', 'email'))
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)

        # write each item
        for item in res:
            w.writerow((item["created"], item["profileUrl"], item["email"]))
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    # stream the response as the data is generated
    response = Response(generate(dbManager.getAllProfilesFromRequest(
        downloadLink)), mimetype='text/csv')
    # add a filename
    response.headers.set("Content-Disposition",
                         "attachment", filename="result.csv")
    return response


@app.route("/database/<string:tableName>", methods=('GET',))
def displayDataBase(tableName):
    """
    Displays database table whose name was filled in the url
    """
    return dbManager.getAllFromTable(tableName)


@app.route("/redis/<string:job_key>", methods=('GET',))
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
