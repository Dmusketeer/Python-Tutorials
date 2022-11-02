# Ask the user to enter the names of three people they want to 
# invite to a party and store them in a list. After they have entered 
# all three names, ask them if they want to add another. If they do, 
# allow them to add more names until they answer “no”. When 
# they answer “no”, display how many people they have invited to 
# the party.

name1,name2,name3=map(str, input("Enter three guest names: ").split())
guestList=[name1,name2,name3]
anotherGuest=input("Do you wanna add more Guests in the list (y/n): ")
while anotherGuest=="y":
    guestList.append(input("Enter Guest Name: "))
    anotherGuest=input("Do you wanna add more Guests in the list (y/n): ")
print(len(guestList))
