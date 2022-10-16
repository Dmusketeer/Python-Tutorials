# Ask the user to enter their favourite colour. If they enter “red”, “RED” or 
# “Red” display the message “I like red too”, otherwise display the message 
# “I don’t like [colour], I prefer red”.

fevColor=input("Enter your fevorite color: ")
if fevColor=="red" or fevColor=="Red" or fevColor=="RED":
    print("I Like red too")
else:
    print(f"I don\'t like {fevColor}, I prefer red.") 
