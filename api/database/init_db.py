import sqlite3

connection = sqlite3.connect('database.db')

# Check whether or not tables exist
with open('schemas.sql') as f:
    connection.executescript(f.read())
    connection.commit()
    connection.close()