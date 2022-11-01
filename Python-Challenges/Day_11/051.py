# Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed with 
# numbers starting from 1.
# Display the dictionary in full, showing the index number and the item.
# Ask them which they want to get rid of and remove it from the list. Sort the remainingdata and display the dictionary. 

UserFavouriteFoods=list(map(str, input("Enter your favourite foods: ").split()))
FoodDictionary={}
for i in range(4):
    FoodDictionary.update({i:UserFavouriteFoods[i]})
print(FoodDictionary)
userChoice=int(input("Enter the index number of the food which you wanna remove: "))
FoodDictionary.pop(userChoice)
print(FoodDictionary)