"""
Working with Files
How to handle data in a file?

Data from an opened file can be read using any of the methods: read, readline and readlines.

Data can be written to a file using either write or writelines method.

A file must be opened, before it is used for reading or writing.


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"""
# Example: Reading a file

fp = open("temp.txt","r") # opening files
# By looping through the lines of the file, you can read the whole file, line by line:
# for line in fp:
#     print(line)
content=fp.read() #reading
# # print(content)
fp.close() # closing




# Writing/creating a file:
# WContent="how to write into a files in python"
# fob=open(r"file.txt","w")
# fob.write(WContent)
# fob.close()



# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
# os.remove("file.txt")



# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("file does't exist!!")




# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

os.rmdir("myfold") # get an error --> [The directory is not empty: 'myfold']

#  *****  Note: You can only remove empty folders.  *****

