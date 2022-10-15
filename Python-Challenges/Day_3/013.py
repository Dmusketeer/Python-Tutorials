# Ask the user to enter a 
# number that is under 
# 20. If they enter a 
# number that is 20 or 
# more, display the 
# message “Too high”, 
# otherwise display 
# “Thank you”. 

Number=int(input("Enter a nummber under 20: "))
if Number >= 20:
    print("Too High")
else:
    print("Thank You")