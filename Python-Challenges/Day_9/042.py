# Display five colours and ask the user to pick one. If they 
# pick the same as the program has chosen, say “Well 
# done”, otherwise display a witty answer which involves 
# the correct colour, e.g. “I bet you are GREEN with envy” 
# or “You are probably feeling BLUE right now”. Ask 
# them to guess again; if they have still not got it right, 
# keep giving them the same clue and ask the user to 
# enter a colour until they guess it correctly.
import random
colorList=["Red","Blue","Green","Black","Maroon"]
print(colorList)
colorChoosenByUser=input("Enter a color from Given list: ")
randomColor=random.choice(colorList).lower()
print(randomColor)
color=True
if colorChoosenByUser==randomColor:
    print("Well Done")
else:
    while color:
        print(f"You are probably feeling {randomColor.capitalize()} right now")
        colorChoosenByUserAgain=input("Enter a color from Given list again: ")
        if colorChoosenByUserAgain==randomColor:
            color=False
