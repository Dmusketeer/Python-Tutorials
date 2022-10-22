# Ask for a number below 50 and then count down from 
# 50 to that number, making sure you show the number 
# they entered in the output.

UserInput=int(input("Enter The Numbers below 50 : "))
for i in range(50,UserInput-1,-1):
    print(i)