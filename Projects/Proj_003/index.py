            # Password Authentication System

import getpass
database={"dheeraj1a":"abcdef","ram2a":"a1b2c3"}
userName=input("Enter user name: ")
Password=getpass.getpass("Enter your password: ")
for i in database.keys():
    if userName==i:
        while Password!=database.get(i):
            Password=getpass.getpass("Enter your password again: ")
        break
else:
    print("Enter the correct user name.")

