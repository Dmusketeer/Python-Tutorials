# Randomly choose a number between 1 and 5. Ask the user to pick a 
# number. If they guess correctly, display the message “Well done”, 
# otherwise tell them if they are too high or too low and ask them to pick a 
# second number. If they guess correctly on their second guess, display 
# “Correct”, otherwise display “You lose”.

import random
comChoice=random.randint(1,5)
userChoice=int(input("Enter a Number: "))
if comChoice==userChoice:
    print("Well Done")

elif userChoice<1:
    print("Too Low")
    userSecChoice=int(input("Enter Number above 1 : "))
    if comChoice==userSecChoice:
        print("Correct")
    else:
        print("You Lose") 
elif userChoice>5:
    print("Too High")
    userSecChoice=int(input("Enter Number below 5 : "))
    if comChoice==userSecChoice:
        print("Correct")
    else:
        print("You Lose") 
else:
    comChoice != userChoice
    userSecChoice=int(input("You are in the range.This is second chance.Enter a Number: "))
    if comChoice==userSecChoice:
        print("Correct")
    else:
        print("You Lose") 