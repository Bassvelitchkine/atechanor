import sqlite3
import json


class DataBaseManager():
    """
    The object that ensures the connection to the database and a series of method that enable interactions
    with this very database
    """

    def __init__(self, dbPath, schemasPath):
        """
        INPUT:
            - str: the path to the database
            - str: path to the sql file where the database was created
        ***
        OUTPUT:
            - None
        ***
        The function initializes our database manager with a path to the database and a path to its schemas.
        """
        self.connection = sqlite3.connect(dbPath, check_same_thread=False)

        with open(schemasPath) as f:
            try:
                self.connection.executescript(f.read())
                self.connection.commit()
                print("\n Database successfully created \n")
            except:
                print("\n Database already exists \n")

        self.connection.row_factory = sqlite3.Row

    def checkInitiator(self, email):
        """
        INPUT:
            - str: email
        ***
        OUTPUT:
            - int or None: the id of the initiator
        ***
        The function checks whether or not the user (of atechanor) exists.
        """
        initiatorEmail = self.connection.execute(
            'SELECT email FROM initiators WHERE email = ?', (email,)).fetchone()
        print("Successfully checked initiator's existence \n")
        return initiatorEmail

    def addInitiator(self, email):
        """
        INPUT:
            - str: initiator's email
        ***
        OUTPUT:
            - int: returns the user id
        ***
        The function checks whether or not the user already exists.
        If he does not exist, adds the instance to the database.
        In all cases, returns the user id attached to the email input.
        """
        initiatorEmail = self.checkInitiator(email)
        if not initiatorEmail:
            sql = 'INSERT INTO initiators (email) VALUES (?)'
            data = (email, )
            self.connection.execute(sql, data)
            self.connection.commit()
        return self.getAllInitiators()

    def getAllInitiators(self):
        """
        INPUT:
            - Connection instance as defined in sqlite3
        ***
        OUTPUT:
            - list of dict: the list of all initiators
        ***
        The function returns of all initiators in the database.
        """
        rows = self.connection.execute('SELECT * FROM initiators').fetchall()
        return json.dumps([dict(elem) for elem in rows])


# def getDBConnection():
#     """
#     INPUT:
#         None
#     OUTPUT:
#         - connection instance as stipulated in the sqlite3 module
#     Connects to the database and returns an object that enables interactions with the database.
#     """
#     conn = sqlite3.connect('database/database.db')
#     conn.row_factory = sqlite3.Row
#     print("Connected to database!")
#     return conn


# def addRequest(connection, request):
#     """
#     INPUT:
#         - connection instance inherited from sqlite3
#         - dict: dictionnary with the email of the request initiator and the requested emails
#     ***
#     OUTPUT:
#         - dict: dictionnary containing the request id as well as the requested profiles.
#     ***
#     The function adds the user to the database and retrieves his id.
#     Then, inserts the new request in the database with the initiator's id inside.
#     Finally, returns the content of the request, i.e the initiator's id and the requested emails that were successfully saved inside the database.
#     """
#     # connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#     #                 (title, content))
#     # connection.commit()
#     # connection.close()
#     print("Add request")
#     return getRequest("stuff")


# def getProfile(profileUrl):
#     """
#     INPUT:
#         - str: stackoverflow profile url
#     ***
#     OUTPUT:
#         - dict: dictionnary with the stackoverflow profile url and the associated email if we found it.
#     ***
#     The function retrieves the info related to a specific stackoverflow user from the database i.e stackoverflow url and email.
#     """
#     print('Got the user profile url!')


# def getProfileList(listProfileUrls):
#     """
#     INPUT:
#         - list of str: the list of all requested stackoverflow profile urls
#     ***
#     OUTPUT:
#         - list of dict: the list of dictionnary with stackoverflow profile urls and associated emails.
#     ***
#     The function retrieves a list of requested profile infos from the database i.e all stackoverflow profile urls and attached emails.
#     """


# def updateRequest():
#     """
#     """


# def getRequest(requestId):
#     """
#     INPUT:
#         - int: the id of a request
#     ***
#     OUTPUT:
#         - dict: dictionnary containing the id of the request and the requested emails.
#     ***
#     The function retrieves the requested id and emails from the database and returns the payload.
#     """
#     print("Got request")
#     return "payload"


# def addProfile(stackoverflow, mail):
#     """
#     INPUT:
#         - str: the stackoverflow profile url
#         - str: email
#     ***
#     OUTPUT:
#         - None
#     ***
#     The function adds a new profile and his attached info inside the database after it's been scraped.
#     """
#     print("Successfully added new profile info")


# def getRequestedProfiles(listRequestedProfiles):
#     """

#     """


# def checkStatus():
#     """
#     """
