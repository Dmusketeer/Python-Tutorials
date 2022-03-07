"""                          Object Relational Mappers
An object-relational mapper (ORM) is a library that automates the transfer of data stored in relational database tables into objects that are adopted in application code.

ORMs offer a high-level abstraction upon a relational database, which permits a developer to write Python code rather than SQL to create, read, update and delete data and schemas in their database.


                             Sample ORM Query
Consider the sample SQL statement used to retrieve employees whose income is 10,000.00.

            " SELECT * FROM EMPLOYEE WHERE INCOME=10000.00 "

The equivalent Django ORM query is

            " emps = Employee.objects.filter(income=10000.00) "

The above code is written in Python and easy to read.

Such an ability to write Python code instead of SQL speeds up web application development.


"""

# Django -> Django ORM -> Psycopg(database connector) -> postgreSql