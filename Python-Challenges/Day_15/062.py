# Define a subprogram that will ask the user to 
# enter a number and save it as the variable 
# “num”. Define another subprogram that will 
# use “num” and count from 1 to that number. 

def userInput():
    num=int(input("Enter a Number: "))
    return num

def countNum():
    for i in range(1,userInput()+1):
        print(i)

countNum()