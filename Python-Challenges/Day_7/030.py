# Ask the user to enter a number between 1 
# and 12 and then display the times table for 
# that number. 

UserInput=int(input("Enter Numbers between 1 to 12 to print it\'s counting: "))
for i in range(1,11):
    print(UserInput*i)
    