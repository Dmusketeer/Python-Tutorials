# Create a list containing the titles of four TV programmes and display them on separate lines.
# Ask the user to enter another show and a position they want it inserted into the list. Display the list again, 
# showing all five TV programmes in their new positions.

name1,name2,name3,name4=map(str, input("Enter three guest names: ").split())
showList=[name1,name2,name3,name4]
anotherShow=input("Enter the name of another tv show: ")
position=int(input("Enter the position of the show: "))
showList.insert(position, anotherShow)
print(showList)