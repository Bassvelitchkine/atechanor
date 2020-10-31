from flask import Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)

@app.route('/submit', methods=('POST'))
def submitRequest():
    """
    """
    if request.method == 'POST':
        email = request.form['email']
        # profilesList = request.form['profilesList']
        print(email)
        return "Success"
        # if not (email or profilesList):
        #     if not email:
        #         flash('Email is required!')
        #     if not profilesList:
        #         flash("A list of profiles is required!")
        # else:
        #     conn = get_db_connection()
        #     addInitiator(conn, email)

@app.route('/download/<int:id>', methods=('GET',))
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

