# Write a new file called 
# “Numbers.txt”. Add five numbers 
# to the document which are stored 
# on the same line and only 
# separated by a comma. Once you 
# have run the program, look in 
# the location where your program is stored and you 
# should see that the file has been 
# created. The easiest way to 
# view the contents of the new text file
# on a Windows system is to read it using Notepad. 


numbers_file=open("Day_14/numbers.txt","w")
numbers_file.write("1,")
numbers_file.write("2,")
numbers_file.write("3,")
numbers_file.write("4,")
numbers_file.write("5,")
numbers_file.close()
