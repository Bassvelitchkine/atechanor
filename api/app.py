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
            # Add request to database
            requestId = dbManager.addRequest(
                {"initiatorId": email, "requestedProfiles": profilesList})
            # Add profiles list to database
            dbManager.addProfiles(profilesList)
            # Link request to requested profiles
            dbManager.connectRequestAndProfiles(requestId, profilesList)
            return "OK"


@app.route('/download/<int:requestId>', methods=('GET',))
def download(requestId):
    """
    """
    # post = get_post(id)
    # conn = get_db_connection()
    # conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    # conn.commit()
    # conn.close()
    # flash('"{}" was successfully deleted!'.format(post['title']))
    # return redirect(url_for('index'))
    return None


@app.route("/database/<string:tableName>", methods=('GET',))
def displayDataBase(tableName):
    """
    Displays database table whose name was filled in the url
    """
    return dbManager.getAllFromTable(tableName)
