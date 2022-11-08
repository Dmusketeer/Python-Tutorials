# Ask the user to type in a word in upper case. If they 
# type it in lower case, ask them to try again. Keep 
# repeating this until they type in a message all in 
# uppercase. 

userInput=input("type in a word in upper case: ")
flag=False
while flag==False:
    if userInput.isupper():
        print("Thank You!")
        flag=True
    else:
        print("Try Again")
        userInput=input("type in a word in upper case: ")

