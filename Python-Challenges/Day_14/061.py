# Display the following menu to the user: 
# 1) Create a new file.
# 2) Display the file.
# 3) Add a new item to the file.
# Make a selection 1,2 or 3.

# Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a 
# suitable error message. If they select 1, ask the user to enter a school 
# subject and save it to a new file called “Subject.txt”. It should overwrite any existing file 
# with a new file. If they select 2, display the contents of the 
# “Subject.txt” file. If they select 3, ask the user to enter a new 
# subject and save it to the file and then display the entire contents of the file.



print("1) Create a new file.")
print("2) Display the file.")
print("3) Add a new item to the file.")
print("Make a selection 1,2 or 3.")

userChoice=int(input("Enter 1, 2 or 3 : "))

if userChoice==1 or userChoice==2 or userChoice==3:
    if userChoice==1:
        subject=input("Enter school subject Names: ")
        file=open("Day_14/Subject.txt","w")
        file.write(subject)
        file.close()
    elif userChoice==2:
        file=open("Day_14/Subject.txt","r")
        print(file.read())
        file.close()
    else:
        pass
        newSubject=input("Enter New subject Names: ")
        file=open("Day_14/Subject.txt","a")
        file.write(newSubject)
        file.close()
        file=open("Day_14/Subject.txt","r")
        print(file.read())
        file.close()
else:
    raise Exception("Enter the Correct Number.")

