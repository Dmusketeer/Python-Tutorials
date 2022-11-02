# Create a list of four three-digit numbers. Display the list to the user, showing each item from the list on a separate line.
# Ask the user to enter a three-digit number. If the number they have typed in matches one in the list, display the position of 
# that number in the list, otherwise display the message “That is not in the list”. 

numberList=[123,345,656,823]
for i in range(len(numberList)):
    print(numberList[i],end="\n")

userChoice=int(input("Enter Number: "))
if userChoice in numberList:
    print(numberList.index(userChoice))
else:
    print("That is not in the list.")
