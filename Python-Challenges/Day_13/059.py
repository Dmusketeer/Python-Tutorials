# Ask the user to enter numbers. If they enter a 
# number between 10 and 20, save it in the array, 
# otherwise display the message “Outside the 
# range”. Once five numbers have been 
# successfully added, display the message “Thank 
# you” and display the array with each item shown 
# on a separate line.
nums=[]
while len(nums)<5:
    userChoice=int(input("Enter a number: "))
    if 10<userChoice<20:
        nums.append(userChoice)
    else:
        print("Outside of the range")
print("Thank You")
for j in range(len(nums)):
    print(nums[j])