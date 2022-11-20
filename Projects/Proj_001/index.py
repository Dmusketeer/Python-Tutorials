                                # Number Guessing Game using Python 

import random
randNum=random.randint(1,10)
userChoice=int(input("Enter a Number between 1 to 10 : "))
while randNum!=userChoice:
    if userChoice<randNum:
        print("Too Low")
        userChoice=int(input("Enter a Number between 1 to 10 : "))
    elif userChoice>randNum:
        print("Too High")
        userChoice=int(input("Enter a Number between 1 to 10 : "))
    else:
        break
print("your guess the right number.")
