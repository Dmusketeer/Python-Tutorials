""" 
                                       Fetching Data
After executing the SQL statement for reading records from a table, either of the following methods can be used to retrieve them in python.

    1.   fetchone: It retrieves one record at a time in the form of a tuple.

    2.   fetchall: It retrieves all fetched records at a point in the form of tuple of tuples.

"""

import sqlite3
# establishing the connection
conn = sqlite3.connect('testdb.db')
# preparing a cursor object
cursor = conn.cursor()
# preparing sql statement
sql = '''
       SELECT * FROM EMPLOYEE
      '''
# executing the sql statement using `try ... except`
try:
    cursor.execute(sql)
except:
    print('Unable to fetch data.')

# fetching the records

records = cursor.fetchall()

for record in records: # Displaying the records
    print(record)

conn.close() # closing the connection
