# Ask the user to enter 
# their name and numbers.then 
# Display 
# their name (one 
# letter at a time on 
# each line) and 
# repeat this for the 
# number of times 
# they entered.

userName=input("Enter Your Name: ")
num=int(input("Enter numbers "))
for i in range(num):
    for j in range(len(userName)):
        print(userName[j])
