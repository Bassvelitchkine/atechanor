import sqlite3

def getDBConnection():
    """
    INPUT: 
        None
    OUTPUT:
        - connection instance as stipulated in the sqlite3 module
    Connects to the database and returns an object that enables interactions with the database.
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    print("Connected to database!")
    return conn

def checkInitiator(connection, email):
    """
    INPUT:
        - connection instance inherited from sqlite3
        - str: email
    ***
    OUTPUT:
        - int or None: the id of the initiator
    ***
    The function checks whether or not the user (of atechanor) exists.
    """
    initiatorEmail = connection.execute('SELECT email FROM initiators WHERE email = ?', (email,)).fetchone()

    if initiatorEmail:
        print("Successfully checked initiator's existence")
        return initiatorEmail
    else:
        print("Successfully checked initiator's existence")
        return None

def addInitiator(connection, email):
    """
    INPUT:
        - connection instance inherited from sqlite3
        - str: initiator's email
    ***
    OUTPUT:
        - int: returns the user id
    ***
    The function checks whether or not the user already exists.
    If he does not exist, adds the instance to the database.
    In all cases, returns the user id attached to the email input.
    """
    initiatorEmail = checkInitiator(connection, email)
    if not initiatorEmail:

    else:
        print("User successfully added to database")
        return initiatorEmail

def addRequest(connection, request):
    """
    INPUT:
        - connection instance inherited from sqlite3
        - dict: dictionnary with the email of the request initiator and the requested emails
    ***
    OUTPUT:
        - dict: dictionnary containing the request id as well as the requested profiles.
    ***
    The function adds the user to the database and retrieves his id. 
    Then, inserts the new request in the database with the initiator's id inside. 
    Finally, returns the content of the request, i.e the initiator's id and the requested emails that were successfully saved inside the database.
    """
    # connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
    #                 (title, content))
    # connection.commit()
    # connection.close()
    print("Add request")
    return getRequest("stuff")

def getProfile(profileUrl):
    """
    INPUT:
        - str: stackoverflow profile url
    ***
    OUTPUT:
        - dict: dictionnary with the stackoverflow profile url and the associated email if we found it.
    ***
    The function retrieves the info related to a specific stackoverflow user from the database i.e stackoverflow url and email.
    """
    print('Got the user profile url!')

def getProfileList(listProfileUrls):
    """
    INPUT:
        - list of str: the list of all requested stackoverflow profile urls
    ***
    OUTPUT:
        - list of dict: the list of dictionnary with stackoverflow profile urls and associated emails.
    ***
    The function retrieves a list of requested profile infos from the database i.e all stackoverflow profile urls and attached emails.
    """
def updateRequest():
    """
    """

def getRequest(requestId):
    """
    INPUT:
        - int: the id of a request
    ***
    OUTPUT:
        - dict: dictionnary containing the id of the request and the requested emails.
    ***
    The function retrieves the requested id and emails from the database and returns the payload.
    """
    print("Got request")
    return "payload"



def addProfile(stackoverflow, mail):
    """
    INPUT: 
        - str: the stackoverflow profile url
        - str: email
    ***
    OUTPUT:
        - None
    ***
    The function adds a new profile and his attached info inside the database after it's been scraped.
    """
    print("Successfully added new profile info")

def getRequestedProfiles(listRequestedProfiles):
    """

    """

def checkStatus():
    """
    """