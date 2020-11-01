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
            - None
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

    def addRequest(self, initiatorId, profileList, nbProfilesToScrape):
        """
        INPUT:
            - initiatorId (str): the email of the initiator
            - profileList (list of str): the list of profile urls requested by the initiator
            - nbProfilesToScrape (int): the number of profiles to process
        ***
        OUTPUT:
            - int: the id of the request we just added
        ***
        The function adds the user to the database and retrieves his id.
        Then, inserts the new request in the database with the initiator's id inside.
        Finally, returns the content of the request, i.e the initiator's id and the requested emails that were successfully saved inside the database.
        """
        rowId = self.connection.execute('INSERT INTO requests (initiatorId, downloadLink, toProcess) VALUES (?,?,?)',
                                        (initiatorId, self.generateLink(initiatorId), nbProfilesToScrape)).lastrowid
        self.connection.commit()
        return rowId

    def addProfiles(self, profilesList):
        """
        INPUT:
            - profilesList (list of str): list of profile urls to add to the database
        OUTPUT:
            - list of str: the list of profiles that are not yet in the database
        Adds the list of profile urls to the database and returns the list of profiles that weren't there before.
        """
        profilesToScrape = []
        nbProfilesToProcess = 0
        for profileUrl in profilesList:
            try:
                self.connection.execute(
                    'INSERT INTO profiles (profileUrl) VALUES (?)', (profileUrl,))
                profilesToScrape.append(profileUrl)
                nbProfilesToProcess += 1
            except:
                res = self.connection.execute(
                    "SELECT email FROM profiles WHERE profileUrl = ?", (profileUrl,))
                email = [dict(elem) for elem in res][0]['email']
                if not email:
                    nbProfilesToProcess += 1
                print("\n Profile already in database \n")

        self.connection.commit()
        return profilesToScrape, nbProfilesToProcess

    def connectRequestAndProfiles(self, requestId, profilesList):
        """
        INPUT:
            - requestId (int): the id of the request
            - profilesList (list of str): the list of all requested profiles
        OUTPUT:
            - None
        ***
        The function connects the request in the requests table to the profile urls in the profiles table.
        """
        self.connection.executemany(
            'INSERT INTO requests_profiles (requestId, profileId) VALUES (?,?)', [(requestId, profileId) for profileId in profilesList])
        self.connection.commit()

    # MODIFYING ELEMENTS IN THE DATABASE #
    def updateProfileEmail(self, profileUrl, email):
        """
        INPUT:
            - urlPortion (str): the stackoverflow url
            - email (str): the email found for the stackoverflow profile
        OUTPUT: 
            None
        ****
        The function updates the profile email in the profiles table as well as the requests in the associated table to see
        if the request is ready.
        """
        self.connection.execute('UPDATE profiles SET email = ?'
                                ' WHERE profileUrl = ?',
                                (email, profileUrl))
        self.connection.commit()

    def updateRequestStatus(self, profileUrl):
        """
        INPUT:
            - profileUrl (str): the profileUrl whose email was eventually found
        OUTPUT:
            - list of str: the list of initiators name whose requests were completed
        ****
        The function updates the profile whose email was eventually found as well as wall requests associated to this profile.
        It returns the list of initiators whose requests were completed.
        """
        initiatorsSatisfied = []

        rows = self.connection.execute(
            'SELECT requestId FROM requests_profiles WHERE profileId = ?', (profileUrl,))
        for row in rows:
            print(row['requestId'])
            self.connection.execute('UPDATE requests SET toProcess = toProcess - 1'
                                    ' WHERE id = ?',
                                    (row["requestId"], ))
            self.connection.commit()
            res = self.connection.execute(
                "SELECT toProcess, initiatorId FROM requests WHERE id = ?", (row["requestId"],))
            resDict = [dict(elem) for elem in res][0]
            toProcess = resDict['toProcess']
            if toProcess == 0:
                initiatorsSatisfied.append(resDict['initiatorId'])
        return initiatorsSatisfied

    # UTILS

    def generateLink(self, initiatorId):
        """
        INPUT:
            - str: id of the initiator
        OUTPUT:
            - str: a hash that will be used to download the result of the request afterwards
        """
        from datetime import datetime
        from hashlib import sha1

        user = initiatorId
        time = str(datetime.now().isoformat())
        plain = user + time
        token = sha1(plain.encode('utf-8'))
        return token.hexdigest()


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
