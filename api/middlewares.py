import sqlite3

# Here are all the middlewares userd throughout the app


# def checkDatabase(function):
#     '''
#     Checking if database exists and creating the database if it does not.
#     '''
#     def modifiedFunction(*args, **kwargs):
#         print("OK")
#         try:
#             connection = sqlite3.connect('database/database.db')
#         except sqlite3.OperationalError:
#             print('Database did not exist')
#             with open('database/schemas.sql') as f:
#                 connection.executescript(f.read())
#                 connection.commit()
#                 connection.close()
#                 print("Database successfully created")
#         return function(*args, **kwargs)

#     modifiedFunction.__name__ = function.__name__
#     return modifiedFunction
