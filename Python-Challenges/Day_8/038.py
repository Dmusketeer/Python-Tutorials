# Randomly choose either heads or tails (“h” or “t”). Ask 
# the user to make their choice. If their choice is the same 
# as the randomly selected value, display the message 
# “You win”, otherwise display “Bad luck”. At the end, tell 
# the user if the computer selected heads or tails.

import random
comChoice=random.choice(["h","t"])
userChoice=input("Enter Head or Tell like h/t : ")
if comChoice==userChoice:
    print("You Win")
else:
    print("Bad Luck")
print(f"Computer select {comChoice}")


