# Topic : Database
#
# The books database has Book table with isbn (int) , title(string), author (string) , price (int)
# For this table perform following CRUD operations:
#
# 1. Insert new book data
# 2. Display data for all books
# 3. Update price for a book
# 4. delete data for a book
# 5. Display books with price >500

import sqlite3
from sqlite3 import Error

def connect_db(path):  #DML Query
    con=None
    try:
        con=sqlite3.connect(path)
        print('connection successful')
        return con
    except Error as e:
        print(e)

def execute_query(con,query,data=None):  #DDL Query
    try:
        cursor=con.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        con.commit()
        print('Query Successful')
    except Error as e:
        print(e)

def execute_read_query(con,query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        results=cursor.fetchall()
        return results
    except Error as e:
        print(e)

def close_connection(con):
    try:
        if con:
            con.close()
    except Error as e:
        print(e)

drop_table = '''DROP TABLE IF EXISTS Books;'''

create_table = '''
CREATE TABLE IF NOT EXISTS Books (
    isbn INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price INTEGER
);'''

insert_books = '''
INSERT OR IGNORE INTO Books (isbn, title, author, price) VALUES 
(101, 'Python Basics', 'John Doe', 450),
(102, 'Advanced AI', 'Jane Smith', 800),
(103, 'Data Science', 'Alice Brown', 600);
'''

insert_book_query = "INSERT OR IGNORE INTO Books (isbn, title, author, price) VALUES (?, ?, ?, ?);"
new_book_data = (104, 'Machine Learning 101', 'Chris Evans', 450)

select_all = "SELECT * FROM Books;"

update_price = "UPDATE Books SET price = 550 WHERE isbn = 101;"

delete_book = "DELETE FROM Books WHERE isbn = 103;"

select_expensive = "SELECT * FROM Books WHERE price > 500;"


path = 'D:\\PGCP_AI_new\\Day7\\books_database.sqlite3'
connection = connect_db(path)

execute_query(connection, drop_table)
execute_query(connection, create_table)

execute_query(connection, insert_books)
print("--- Books Before Insertion ---")
for book in execute_read_query(connection, select_all):
    print(book)

print("\n--- Inserting New Book ---")

execute_query(connection, insert_book_query, new_book_data)
print("--- Books After Insertion ---")
for book in execute_read_query(connection, select_all):
    print(book)


print("\n--- Updating Price ---")
execute_query(connection, update_price)
for book in execute_read_query(connection, select_all):
    print(book)

print("\n--- Deleting ---")
execute_query(connection, delete_book)
for book in execute_read_query(connection, select_all):
    print(book)

print("\n--- Books with Price > 500 ---")
for book in execute_read_query(connection, select_expensive):
    print(book)

if connection:
    connection.close()




