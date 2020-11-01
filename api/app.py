from flask import Flask, render_template, request, url_for, flash, redirect
from .dataBaseManager import DataBaseManager

dbManager = DataBaseManager('database/database.db', 'database/schemas.sql')
app = Flask(__name__)


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
            return "OK"


@app.route('/update/<string:urlPortion>/<string:email>', methods=('PUT',))
def updateProfileEmail(urlPortion, email):
    """
    INPUT:
        - urlPortion (str): the part of the url that differenciates several stackoverflow users
        - email (str): the email found for the stackoverflow profile
    OUTPUT: None
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

    return None


@app.route("/database/<string:tableName>", methods=('GET',))
def displayDataBase(tableName):
    """
    Displays database table whose name was filled in the url
    """
    return dbManager.getAllFromTable(tableName)
