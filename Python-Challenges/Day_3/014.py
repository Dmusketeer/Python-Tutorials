# Ask the user to enter a 
# number between 10 and 20 
# (inclusive). If they enter a 
# number within this range, 
# display the message “Thank 
# you”, otherwise display the 
# message “Incorrect 
# answer”. 

Number=int(input("Enter a nummber under 20: "))
if Number >= 10 and Number <= 20:
    print("Thank You")
else:
    print("Incorrect answer")