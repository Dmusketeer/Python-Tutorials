# Ask the user to enter their 
# name and a number. If the 
# number is less than 10, then 
# display their name that 
# number of times; otherwise 
# display the message “Too 
# high” three times. 


userName=input("Enter Your Name: ")
num=int(input("Enter numbers "))
if num<10:
    for i in range(1,num+1):
        print(userName)
else:
    for i in range(3):
        print("Too high")