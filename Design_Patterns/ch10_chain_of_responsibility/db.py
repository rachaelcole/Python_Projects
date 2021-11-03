import sqlite3
from logger import Logger

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        Logger.error(e)
    return conn

def create_project(conn, project):
    """Create a new project into the projects table"""
    sql = '''INSERT INTO projects(name,begin_date,end_date,values'''


DATABASE_URL = 'Users.db'
conn = create_connection(DATABASE_URL)
db = conn.cursor()

# Run db.execute("SQLITE3 COMMAND") etc to execute commands:

# Create table
#db.execute('''CREATE TABLE Users 
#             (id INTEGER PRIMARY KEY, token TEXT, name TEXT)''')

# Insert a row of data
db.execute("INSERT INTO Users VALUES (1, 'akesot', 'Mark')")

# Save (commit) the changes:
conn.commit()

# Close the connection:
db.close()