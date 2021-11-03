# Chain of Responsibility pattern

import sqlite3
from logger import Logger

# One component of web frameworks is the middleware layer. The middleware sits between the client making requests and the actual
# application. Both requests from the client and responses from the application need to pass through the middleware. Middleware
# can include logging functions for incoming requests and outgoing responses, check the user's access and whether they should
# be allowed to execute the request they are making, translation of data, escaping input values, etc.

# Most web frameworks (c.f. Flask, Django) create a request and response object that is used throughout the system, such as these 
# extremely simple example classes:
class Request(object):
    def __init___(self, headers, url, body, GET, POST):
        self.headers = headers
        self.url = url
        self.body = body
        self.GET = GET
        self.POST = POST
        Logger.info(headers, url, body, 'GET =', GET, 'POST =', POST)

class Response(object):
    def __init__(self, headers, status_code, body):
        self.headers = headers
        self.status_code = status_code
        self.body = body
        Logger.info(headers, status_code, body)
    
# We would like our middleware to check for a token in the Request object's headers and then add the User object to the object.
# We will write a function that grabs a user token and loads a User() object from a Sqlite database, and return a User() object 
# that can be attached to the request object

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        Logger.error(e)
    return conn
# Connect to the database:
DATABASE_URL = 'Users.db'
conn = create_connection(DATABASE_URL)
db = conn.cursor()

# A User class that gets stored in the database
class User(object):
    def __init__(self, token, name):
        self.token = token
        self.name = name
        params = token, name
        # Save User to the db:
        db.execute('INSERT INTO Users(token, name) VALUES(?, ?)', params)
        # Save (commit) the changes:
        conn.commit()
    # Find a user by their token
    def find_user(token):
        db.execute('SELECT * FROM Users WHERE (token = ?)', (token,))
        matches = []
        for user in db:
            print(user)
            matches.append(user)
        return matches

# Calling the User() object with token and name params:
# luke = User('sjvodh', 'Luke')

# Display all the rows of the table:
db.execute('SELECT * FROM Users')
for row in db:
    print(row)

# Find a user by their token:
User.find_user('sjvodh')

# Close the connection:
db.close()


# Reference: 
# Badenhurst, Wessel. "Chapter 10: Chain of Responsibility Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 143-165,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_10.