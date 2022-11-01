# Create a tuple containing the names of five countries and display the whole tuple. 
# Ask the user to enter one of the countries that have been shown to them and then display 
# the index number (i.e. position in the list) of that item in the tuple. 

country_tuple=("india","usa","uk","south africa","australia")
print(country_tuple)
user_preference=input("Enter country Name from the above tuple: ")
print(country_tuple.index(user_preference))


