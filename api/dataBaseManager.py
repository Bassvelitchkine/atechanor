import sqlite3
import json


class DataBaseManager():
    """
    The object that ensures the connection to the database and a series of method that enable interactions
    with this very database
    """
    # INITIALIZATION #

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

    # RETRIEVING ELEMENTS FROM THE DATABASE #
    def getInitiator(self, initiatorId):
        """
        INPUT:
            - str or int: id of the requested element
        ***
        OUTPUT:
            - int or str or None: the id of the sought element
        """
        return self.connection.execute(
            f'SELECT email FROM initiators WHERE email = ?', (initiatorId,)).fetchone()

    def getRequest(self, requestId):
        """
        INPUT:
            - str or int: id of the requested element
        ***
        OUTPUT:
            - int or str or None: the id of the sought element
        """
        return self.connection.execute(
            f'SELECT * FROM requests WHERE id = ?', (requestId,)).fetchone()

    def getAllFromTable(self, tableName):
        """
        INPUT:
            - str: name of the table in the data base
        ***
        OUTPUT:
            - list of dict: the list of all initiators
        ***
        The function returns all instances in the table passed as argument.
        """
        rows = self.connection.execute(f'SELECT * FROM {tableName}').fetchall()
        return json.dumps([dict(elem) for elem in rows])

    # ADDING ELEMENTS TO THE DATABASE #
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
        initiatorEmail = self.getInitiator(email)

        if not initiatorEmail:
            sql = 'INSERT INTO initiators (email) VALUES (?)'
            data = (email, )
            self.connection.execute(sql, data)
            self.connection.commit()
            print("Initiator successfully created \n")

        return [str(elem) for elem in self.getInitiator(email)][0]

    def addRequest(self, request):
        """
        INPUT:
            - dict: dictionnary with the email of the request initiator and the requested emails
        ***
        OUTPUT:
            - dict: dictionnary containing the request id as well as the requested profiles.
        ***
        The function adds the user to the database and retrieves his id.
        Then, inserts the new request in the database with the initiator's id inside.
        Finally, returns the content of the request, i.e the initiator's id and the requested emails that were successfully saved inside the database.
        """
        rowId = self.connection.execute('INSERT INTO requests (initiatorId) VALUES (?)',
                                        (request["initiatorId"],)).lastrowid
        self.connection.commit()
        return [str(elem) for elem in self.getRequest(rowId)]

    def addProfiles(self, profilesList):
        """
        INPUT:
            - profilesList (list of str): list of profile urls to add to the database
        OUTPUT:
            - None
        Adds the list of profile urls to the database.
        """
        for profileUrl in profilesList:
            try:
                self.connection.execute(
                    'INSERT INTO profiles (profileUrl) VALUES (?)', (profileUrl,))
            except:
                print('Profile already in database')

        self.connection.commit()
        return self.getAllFromTable("profiles")


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
