# Randomly pick a whole number between 1 
# and 10. Ask the user to enter a number and 
# keep entering numbers until they enter the 
# number that was randomly picked. 

import random
randNum = random.randint(1, 11)
userInput=int((input("Enter a Number : ")))
while(randNum!=userInput):
    userInput=int((input("Enter the Number again : ")))

print("Right guess")
