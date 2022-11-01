# Create a list of six school subjects. Ask the user which of these 
# subjects they don’t like. Delete the subject they have chosen from the 
# list before you display the list again.

subList=["math","science","history","commerce","hindi","english"]
userChoice=input("Enter subject which you don't like: ")
subList.remove(userChoice)
print(subList)