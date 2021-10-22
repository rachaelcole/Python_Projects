# When we create a database table we must tell the db in advance the names of each of the columns, and the types of
# data we plan to store in each column. I.e., data structures must be designed before programming begins.

# In this file we will create a database (db) file named `Tracks` with two columns

import sqlite3

# Make connection to the db stored in the file `music.sqlite` in the current directory:
conn = sqlite3.connect('music.sqlite')

# A cursor is like a file handle we can use to perform operations on the data stored in the db:
cur = conn.cursor()

# Execute commands on the db using the execute() method:
cur.execute('DROP TABLE IF EXISTS Tracks')  # DROP removes the table if it exists in the db
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')  # CREATEs the table with 2 columns, 'title' and 'plays'

# Add data to the db using INSERT:
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
conn.commit()  # forces the data to be written to the db file

# Print the data:
print('Tracks:')
# Grab the data you want to print using SELECT 'data you want' FROM 'db name':
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
# Delete data using DELETE FROM 'db name' WHERE 'condition you choose':
cur.execute('DELETE FROM Tracks WHERE plays < 25')  # deletes all entries where plays are less than 25
conn.commit()  # write your execution to the db file

cur.close()  # closes the connection to the db
