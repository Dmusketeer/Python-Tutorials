"""

                                Python Database API

How to connect to Python database?

Python Database API (DB-API) is a standard interface to interact with various databases.

DB-API supports connecting to different database servers such as Microsoft SQL Server 2000, PostgreSQL, Oracle.

Different DB API’s are used for accessing different databases. Hence a programmer has to install DB API corresponding to the database one is working with.



                                Working with a Database

Working with a database includes the following steps:

        Importing the corresponding DB-API module.

        Acquiring a connection with the database.

        Executing SQL statements and stored procedures.

        Closing the connection



"""

# sqlite3 is available by default in Python standard library and hence there is no need of installing it separately.

# SQLite is a very lightweight database. You can connect to it directly, with minimal settings.




# Creating a Sample Table


import sqlite3 
conn = sqlite3.connect("testdb.db") # establising the database connection
cursor = conn.cursor() # preparing a cursor object
sql1 = 'DROP TABLE IF  EXISTS EMPLOYEE'

sql2 = '''

       CREATE TABLE EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )   
    
    '''
# executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)

# closing the connection
conn.close()
