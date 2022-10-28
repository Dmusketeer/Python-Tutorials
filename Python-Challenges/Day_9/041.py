# Make a maths quiz that asks five questions by randomly 
# generating two whole numbers to make the question 
# (e.g. [num1] + [num2]). Ask the user to enter the 
# answer. If they get it right add a point to their score. At 
# the end of the quiz, tell them how many they got correct 
# out of five.


import random
score=0
for i in range(5):    
    randomlst=random.sample(range(1,1000), 2)
    print(f"{randomlst[0]} + {randomlst[1]}")
    num=randomlst[0]+randomlst[1]
    answer=int(input("Try to guess correct Number: "))
    if answer==num:
        score=+1
print(f"Your score {score} out of 5")
    

