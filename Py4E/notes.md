# Object-Oriented Programming
Reference: [https://www.py4e.com/html3/14-objects](https://www.py4e.com/html3/15-database)

- `stuff = list()`                     Constructs an object of type list


- `stuff.append('rachael') `           Call `append()` method 


- `stuff.sort()`                        Call the `sort()` method 


- `print(stuff[0]) `                    Retrieve the item at index 0 


- `print(stuff.__getitem__(0))`         Call the `__getitem__()` method in the stuff list with a parameter of 0 


- `print(list.__getitem__(stuff, 0))`   Call the `__getitem__()` method in the list object with parameters of stuff and 0 


- `print(dir(stuff)) `                  Prints all the capabilities of the stuff object (its methods)


OOP can hide complexity. It allows us to focus on parts of the program we need to solve and ignore other parts of the
program. At a basic level, an object is some code plus data structures that is smaller than a whole program. Defining
a function allows us to store a bit of code, give it a name, and later invoke that code using the name of the
function. An object can contain a number of functions, called methods, as well as data used by those functions. Data
items that are part of an object are called attributes. We use the `class` keyword to define the data and code that
will make up each of the objects.

# Databses and SQL
Reference: [https://www.py4e.com/html3/15-database](https://www.py4e.com/html3/15-database)

Databases can be useful when:
1. Your app needs to make many small random updates within a large data set
2. Your data is so large it cannot fit in a dictionary, and you need to look up information repeatedly
3. You have a long-running process that you want to be able to stop and restart and retain the data from one run to the next.

It is important to plan and follow the rules of data normalisation when designing a database.

When we create a database table we must tell the db in advance the names of each of the columns, and the types of
data we plan to store in each column. I.e., data structures must be designed before programming begins.

**Structured Query Language (SQL)** was developed as a standard for communicating with database systems.

A relational database is made up of tables, which are made up of columns and rows. Columns generally have a type, such
as text, numeric, or date data. When we create a table, we must specify the names and types of each of the columns:

`CREATE TABLE Tracks (title TEXT, plays INTEGER)`

To insert a row into a table, we use the SQL `INSERT` command:

`INSERT INTO Tracks (title, plays) VALUES ('My Way', 15)`

The `INSERT` statement specifies the table name, then the columns you would like to set in the new row, and then the 
keyword `VALUES` and the corresponding values for each of the fields.

The SQL `SELECT` command is used to retrieve rows and columns from a database. It lets you specify which columns you
would like to retrieve as well as a `WHERE` clause to select which rows you would like to see. It has an optional 
`ORDER BY` clause to control the sorting of the returned rows.

`SELECT * FROM Tracks WHERE title = 'My Way'`

Using `*` selects all the columns for each row that matches the `WHERE` clause.

You can request rows be sorted by one of the columns:

`SELECT title, plays FROM Tracks ORDER BY title`

To remove a row, you need a `WHERE` clause on a `DELETE` statement:

`DELETE FROM Tracks WHERE title = 'My Way'`

You can update columns within one or more rows using `UPDATE` as follows:

`UPDATE Tracks SET plays = 16 WHERE title = 'My Way'`

### Basic data modelling
Deciding how to break up your app data into multiple tables and establishing relationships between those tables is
called _data modelling_.

A best practice for _data normalisation_ states we should never put the same string data in the database more than 
once. If we need the data more than once, we use a numeric _key_ for the data and reference the actual data using this
key.

Databases should contain an `id` column that takes an `INTEGER PRIMARY KEY` type. This indicates that we want SQLite
to manage this column and assign a unique numeric key to each row we insert automatically. 

We can also add a `UNIQUE` clause to our table columns, which indicates we will not allow two rows to hold the same 
value for the specified `UNIQUE` column.

There are generally three kinds of keys used in a database model:

- A _logical key_ is one a user might use to look up a row, such as 'name'; it often makes sense to add a `UNIQUE` constraint to a logical key
- A _primary key_ is an integer assigned by the database, by convention stored in the `id` column
- A _foreign key_ is usually a number that points to the primary key of an associated row in a different table

### Retrieving data with JOIN
SQL uses the `JOIN` clause to connect tables in a database, specifying the fields used to connect the rows between the
tables. For example:

`SELECT * FROM Follows JOIN People ON Follows.from_id = People.id WHERE People.id = 1`

- The `JOIN` clause indicates the fields we are selecting cross both the `Follows` and `People` tables.

- The `ON` clause indicates how the two tables are to be joined.

- Take the rows from `Follows` and append the row from `People` `WHERE` the field `from_id` in `Follows` is the same as 
the `id` value in the `People` table.

The result of the `JOIN` is to create long meta-rows which have both the fields from `People` and the fields from
`Follows`. Where there is more than one match between the `id` field from `People` and the `from_id` from `Follows`, 
then `JOIN` creates a metarow for _each_ of the matching pairs of rows, duplicating data as needed.
