# Define a subprogram that will ask the user to pick a low and a high number, and then generate a random 
# number between those two values and store it in a variable called “comp_num”. 
# 
# Define another subprogram that will give the instruction “I am thinking of a number…” and then ask the user to 
# guess the number they are thinking of.
# 
# Define a third subprogram that will check to see if the comp_num is the same as 
# the user’s guess. If it is, it should display the message “Correct, you win”, otherwise it should
# keep looping, telling the user if they are too low or too high and asking them 
# to guess again until they guess correctl.

import random

def randomNumber():
    '''Generate a random number between two numbers'''
    num1=int(input("Enter Lower num: "))
    num2=int(input("Enter higher num: "))
    comp_num=random.randint(num1, num2)
    return comp_num

# print(randomNumber())

def userGuessNumber():
    print("I am thinking of a number... ")
    userGuess=int(input("Enter the number you guess: "))
    return userGuess

def equalityCheck():
    check_again=True
    while check_again==True:
        if randomNumber()==userGuessNumber():
            print("Correct You win")
            check_again=False
        elif randomNumber() > userGuessNumber():
            userGuess=int(input("Two Low! Guess Again: "))
        else:
            userGuess=int(input("Two High! Guess Again: "))
                

equalityCheck()



