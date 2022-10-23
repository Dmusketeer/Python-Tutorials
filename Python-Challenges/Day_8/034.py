# Ask which direction the user wants to count (up or down). If they select up, then ask 
# them for the top number and then count from 1 to that number. If they select down, ask 
# them to enter a number below 20 and then count down from 20 to that number. If they 
# entered something other than up or down, display the message “I don’t understand”. 

userDirection=input("Enter the direction you want to count like up or down: ")
if userDirection=="up":
    upNum=int(input("Enter the top number: "))
    for upCount in range(1,upNum+1):
        print(upCount)
elif userDirection=="down":
        downNum=int(input("Enter the number below 20: "))
        for downCount in range(20,downNum-1,-1):
            print(downCount)
else:
    print("I don\'t understand.")
