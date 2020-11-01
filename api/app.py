from flask import Flask, render_template, request, url_for, flash, redirect
from .dataBaseManager import DataBaseManager

dbManager = DataBaseManager('database/database.db', 'database/schemas.sql')
app = Flask(__name__)


@app.route('/submit', methods=('POST',))
def submitRequest():
    """
    """
    if request.method == 'POST':
        email = request.form['email']
        profilesList = request.form['profilesList']

        if not (email or profilesList):
            if not email:
                flash('Email is required!')
            if not profilesList:
                flash("A list of profiles is required!")
        else:
            initiatorId = dbManager.addInitiator(email)
            return dbManager.addRequest({"initiatorId": initiatorId, "requestedProfiles": profilesList})


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
