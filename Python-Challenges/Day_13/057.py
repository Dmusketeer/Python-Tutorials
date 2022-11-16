# Ask the user for a list of five 
# integers. Store them in an array. 
# Sort the list and display it in 
# reverse order.

from array import *
arr=array('i',[])
more=int(input("enter number of integer: "))
for i in range(0,more):
    arrVal=int(input("Enter arr value: "))
    arr.append(arrVal)
arr=sorted(arr)
arr.reverse()
print(arr)

