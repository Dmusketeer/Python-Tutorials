# Ask how many slices of pizza the user  started with and ask  how many slices they have eaten. 
# Work out how many slices they have left and display the  answer in a user friendly format. 

startedSlices=int(input("how many slices of pizza do you want ? "))
eatenSlices=int(input("how many slices ha sbeen eaten ?"))
leftSlices = startedSlices-eatenSlices
print(f"{leftSlices} slices has been left!!")

