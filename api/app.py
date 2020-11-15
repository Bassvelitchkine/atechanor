from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from dataBaseManager import DataBaseManager
from io import StringIO
from werkzeug.wrappers import Response
from rq import Queue
from rq.job import Job
from emailScraper import emailScraper
import redis
from flask_cors import CORS
import os
from ElasticEmailClient import ApiClient, Account, Email

# Flask app
app = Flask(__name__)
# Environment
if os.environ['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
    print("\n DEVELOPMENT ENVIRONMENT \n")
if os.environ['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
    print("\n PRODUCTION ENVIRONMENT \n")

# Database connection
dbManager = DataBaseManager('database/database.db', 'database/schemas.sql')
# Reddis and queue
conn = redis.from_url("redis://redis:6379")
q = Queue(connection=conn, default_timeout=1000)
# CORS policies
cors = CORS(app)


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

    try:
        emails = ",".join(request.json["emails"])
    except:
        emails = ""

    # Let's update first the profile whose email was eventually found
    dbManager.updateProfileEmail(profileUrl, emails)

    # Let's update requests that have said profile in their request
    initiatorStatisfied = dbManager.updateRequestStatus(profileUrl)

    # Send download link to initiators satisfied
    for initiator in initiatorStatisfied:
        downloadLink = app.config['DOWNLOAD_DOMAIN'] + \
            ":5000/download/" + initiator[1]
        emailResponse = Email.Send(
            template="exportReady", isTransactional=True, merge={"downloadLink": downloadLink}, msgTo=[initiator[0]])

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
