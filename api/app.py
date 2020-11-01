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
            initiatorId = dbManager.addInitiator(email)
            print("\n " + "initiatorId: " + initiatorId + "\n")
            # Add request to database
            addedRequest = dbManager.addRequest(
                {"initiatorId": initiatorId, "requestedProfiles": profilesList})
            print("Request: " + " // ".join(addedRequest) + "\n")
            # Add profiles list to database
            return dbManager.addProfiles(profilesList)


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
