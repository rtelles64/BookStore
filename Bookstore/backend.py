'''
This is our backend (database) file

We make this app into an OOP version
'''

import sqlite3

class Database:

    # a function that connects to the database
    # any word can be passed to init but by convention we use 'self'
    def __init__(self, db): # required for python OOP (similar to default constructor)
        self.conn = sqlite3.connect(db) # remember to establish connection!
        self.cur = self.conn.cursor() # create cursor object
        # execute SQL segment
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, \
                                                      title text, \
                                                      author text, \
                                                      year integer, \
                                                      isbn integer)")
        self.conn.commit() # commit changes
        #conn.close() # close connection

    # a function that inserts information into the database
    def insert(self, title, author, year, isbn):
        # we create a new connection as opposed to calling the function because
        # the function closes the connection
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        # NULL parameter creates id automatically
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",\
                    (title, author, year, isbn))
        self.conn.commit()
        #self.conn.close()

    # a function that fetches all rows of the table
    def view(self):
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        # NULL parameter creates id automatically
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        #self.conn.close()

        return rows

    # a function that searches for an entry
    # emptry strings are passed as default values, so as not to require values
    # for these specific entries
    def search(self, title = "", author = "", year = "", isbn = ""):
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        # NULL parameter creates id automatically
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ?\
                    OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        #self.conn.close()

        return rows

    # a function that deletes a record (entry)
    def delete(self, id):
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        # the first id is the column name, and the second is the id parameter
        # don't confuse the two!
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()
        #self.conn.close()

    # a function that updates records
    # (i.e. updates id, with the remaining 4 values)
    def update(self, id, title, author, year, isbn):
        #conn = sqlite3.connect("books.db")
        #cur = conn.cursor()
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? \
                     WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()
        #self.conn.close()

    def __del__(self): # destructor method
        self.conn.close()

# debug statements
#insert("The Sun", "John Smith", 1918, 913135132)
#delete(2)
#update(3, "The Moon", "John Smooth", 1917, 987654321)
#print(view())
#print(search(author = "John Smith"))
