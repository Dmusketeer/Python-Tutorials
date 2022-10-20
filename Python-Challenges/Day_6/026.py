# Display the following message: 
# 1)Square
# 2)Triangle

# Enter  a number: 

# If the user enters 1, then it should ask them for 
# the length of one of its sides and display the 
# area. If they select 2, it should ask for the base 
# and height of the triangle and display the area. If 
# they type in anything else, it should give them a 
# suitable error message.

print("1)Square")
print("2)Trinangle")
userInput=int(input("Enter a Number: "))
if userInput==1:
    side=int(input("Enter the Length of one of Square sides: "))
    print(f"Area of the triangle is {side*side}")
elif userInput==2:
    base,height=map(int,input("Enter the base and height of the triangle: ").split())
    print(f"Area of the triangle is {(base*height)/2}")
else:
    print("Enter valid number") 
    
