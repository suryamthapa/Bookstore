"""
So, this is the backend process of the dictionary project.
This file will be imported in the frontend file and these
functions will be used there.
--------------
Learnings:
--------------
1. About sqlite module
Basically, i was familier with sql databases shortly.
And i knew about the servers/datebases and simple sql queries.
And i have worked with mysql.connector module.
But i had no idea that we can have a database as a file(.pd), and it can be modified as per our wish.
So, it was fun to work with sqlite3.
It is quite similar to the mysql.connector.
"""
import sqlite3

# connecting to the database
def connect():
    global cursor
    global conn
    conn = sqlite3.connect("bookdata.pd")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title varchar(55),author text, year integer,isbn integer)")
    # cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,title varchar(55),author text, year integer,isbn integer)")
    # cursor.execute("DROP TABLE book")
    conn.commit()
# Inserting datas 
def insert(title,author,year,isbn):
    cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
# viewing the existing datas
def view():
    cursor.execute("SELECT * FROM book")
    result = cursor.fetchall()
    return result
# Searching the datas
def search(title="",author="",year="",isbn=""):
    cursor.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=? ",(title,author,year,isbn))
    result = cursor.fetchall()
    return result
# deleting the data
def delete(id):
    cursor.execute("DELETE FROM book where id=?",(id,))
    conn.commit()
# updating the data
def update(id,title,author,year,isbn):
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
# connecting to the database
connect()