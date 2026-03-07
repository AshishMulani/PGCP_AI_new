import mysql.connector as mysql
from mysql.connector import Error

# mydb=mysql.connect
def connect_db(username,password,dbname,host='localhost',port=3306):
    con=None
    try:
        con=mysql.connect( host=host,
            user=username,password=password,databasename=dbname,port=port)
        if con.is_connected():
            print('connection successful')
        return con
    except Error as e:
        print(e)

def execute_query(con,query):
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


create_table='''CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,          
    FirstName VARCHAR(50) NOT NULL,     
    LastName VARCHAR(50) NOT NULL,       
    Email VARCHAR(100) UNIQUE,           
    HireDate DATE NOT NULL,             
    Salary DECIMAL(10, 2) CHECK (Salary >= 0),
    DepartmentID INT,                    
    CONSTRAINT fk_department FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
)'''

insert='''INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, HireDate, Salary, DepartmentID)
VALUES 
(1, 'John', 'Doe', 'john.doe@example.com', '2024-01-15', 50000.00, 101),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '2023-11-20', 60000.00, 102);
'''

update='''UPDATE Employees
SET Salary = 55000.00, DepartmentID = 103
WHERE EmployeeID = 1;
'''

delete='''DELETE FROM Employees
WHERE EmployeeID = 2;
'''
select = '''SELECT * FROM Employees;'''


connection = connect_db("root", "root", "testdb")

execute_query(connection, create_table)
execute_query(connection, insert)

print("\n--- Employees After Insert ---")
rows = execute_read_query(connection, select)
for row in rows:
    print(row)

execute_query(connection, update)
print("\n--- Employees After Update ---")
rows = execute_read_query(connection, select)
for row in rows:
    print(row)

execute_query(connection, delete)
print("\n--- Employees After Delete ---")
rows = execute_read_query(connection, select)
for row in rows:
    print(row)

close_connection(connection)