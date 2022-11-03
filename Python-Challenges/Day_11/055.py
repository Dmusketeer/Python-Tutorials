# Create an empty list called “nums”. Ask the user to enter numbers. 
# After each number is entered, add it to the end of the nums list and 
# display the list. Once they have entered three numbers, ask them if 
# they still want the last number they entered saved. If they say “no”, 
# remove the last item from the list. Display the list of numbers. 

nums=[]
for i in range(3):
    userInput=int(input("Enter Number: "))
    nums.append(userInput)
if len(nums)==3:
    userPole=input("you still want to save the last number which you have entered ? (y/n)")
    if userPole=="n":
        nums.pop()
print(nums)

