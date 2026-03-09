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

def execute_query(con,query):  #DDL Query
    try:
        cursor=con.cursor()
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


create_table='''CREATE TABLE IF NOT EXISTS Books
(BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    BookName TEXT NOT NULL,
    Price INTEGER 
);'''

add_users='''INSERT INTO Books (BookName, Price)
VALUES
('John', 30),
('Jane', 25),
('Alice', 28);'''

update_user = '''
UPDATE User
SET Price = 31
WHERE BookName = 'John';
'''

delete_user = '''
DELETE FROM User
WHERE BookName = 'Alice';
'''

select_users = '''
SELECT * FROM User;
'''

path='D:\\PGCP_AI_new\\Day7\\Users.sqlite3'
connection=connect_db(path)

# execute_query(connection, drop_table)
execute_query(connection,create_table)
execute_query(connection,add_users)


users=execute_read_query(connection,select_users)
for user in users:
    print(user)

execute_query(connection,update_user)
users=execute_read_query(connection,select_users)
for user in users:
    print(user)

execute_query(connection,delete_user)
users=execute_read_query(connection,select_users)
for user in users:
    print(user)