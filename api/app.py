from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from dataBaseManager import DataBaseManager
from io import StringIO
from werkzeug.wrappers import Response
# from rq import Queue
# from rq.job import Job
# from .scraper.worker import conn
# from .scraper.emailScraper import emailScraper

dbManager = DataBaseManager('database/database.db', 'database/schemas.sql')
app = Flask(__name__)

# q = Queue(connection=conn)


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

            # # Add tasks to the queue
            # for profileUrl in profilesToScrape:
            #     job = q.enqueue_call(
            #         func=emailScraper, args=(profileUrl,), result_ttl=5000)
            #     print("\n Job id: " + job.get_id() + "\n")

            return "OK"


@app.route('/update/<string:urlPortion>/<string:email>', methods=('PUT',))
def updateProfileEmail(urlPortion, email):
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
    profileUrl = "https://stackoverflow.com/users/" + urlPortion + "/view"
    # Let's update first the profile whose email was eventually found
    dbManager.updateProfileEmail(profileUrl, email)
    # Let's update requests that have said profile in their request
    initiatorStatisfied = dbManager.updateRequestStatus(profileUrl)
    print("\n initiators satisfied: " + " // ".join(initiatorStatisfied))
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
