# Create an array which will store a list of integers. 
# Generate five random numbers and store them in 
# the array. Display the array (showing each item on 
# a separate line). 


import random
from array import * 
arr=array("i",[])
for i in range(5):
    num=random.randint(0, 9)
    arr.append(num)
for i in arr:   
    print(i)