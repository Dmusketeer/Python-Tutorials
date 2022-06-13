import sqlite3
conn= sqlite3.connect('testdb.db')#establishing a connection
cursor=conn.cursor()# preparing a cussor object
rec=[

    (123456, 'John', 25, 'M', 50000.00),

    (234651, 'Juli', 35, 'F', 75000.00),

    (345121, 'Fred', 48, 'M', 125000.00),

    (562412, 'Rosy', 28, 'F', 52000.00)


    ]

sql='''
    INSERT INTO EMPLOYEE VALUES(?,?,?,?,?)
    '''

# executing sql block using try....except blocks

try: 
    cursor.executemany(sql,rec)
    conn.commit()
except Exception as e:
    print("Error message : ",str(e))
    conn.rollback()

# closing the database connection
conn.close()


#   ***  NOTE : A single record is inserted into table EMPLOYEE.  ***
