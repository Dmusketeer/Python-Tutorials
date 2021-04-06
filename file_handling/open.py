f = open("exp.txt", 'rt') #r-read,t-text so read in text mode
print(f)  # The open() function returns a file object, which has a read() method.
print(30*'-')


# # if the file is at same directory
f = open("exp.txt", 'rt')
print(f.read())  # 
print(30*'-')

# # open a file at  different location
f = open(r"C:\Users\DHEERAJ TIWARI\Desktop\doc.txt", 'rt')
print(f.read()) 
print(30*'-')


# # Read Only Parts of the File
f=open('exp.txt','r')
print(f.read(5))  # Return the 5 first characters of the file
print(30*'-')


# Read Lines
f=open('exp.txt','r')
# Read one line of the file.
print(f.readline())
# By calling readline() two times, you can read the two first lines:
print(30*'-')


# By looping through the lines of the file, you can read the whole file, line by line:
f=open('exp.txt','r') 
for i in f:
    print(i)
print(30*'-')

# Close Files
f=open('exp.txt','r')
print(f.readline())
f.close()
# note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
print(30*'-')



# Python File Write
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content


f=open('exp.txt','a')
f.write('Now the file has more content!')
f.close()

f=open('exp.txt','r')
print(f.read())
print(30*'-')




f = open(r'C:\Users\DHEERAJ TIWARI\Desktop\doc.txt', 'r')
print(f.read())

# "w" method will overwrite the entire file.
f = open(r'C:\Users\DHEERAJ TIWARI\Desktop\doc.txt', 'w')
f.write('woops I have deleted the content!')
f.close()

f=open(r'C:\Users\DHEERAJ TIWARI\Desktop\doc.txt','r')
print(f.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist
# Example:
f = open('newfile.txt', 'x')  # Create a file called "newfile.txt":



# Delete a File
# To delete a file, we must import the OS module, and run its os.remove() function
import os
os.remove('newfile.txt')


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists('newfile.txt'):
    os.remove('newfile.txt')
else:
    print('file don\'t exist!')


# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
# Remove the folder "myfolder":

import os 
os.rmdir('myfolder')  # You can only remove empty folders

# Note: You can only remove empty folders.
