# Ask for two numbers. If 
# the first one is larger 
# than the second, display 
# the second number first 
# and then the first 
# number, otherwise show 
# the first number first and 
# then the second. 

num1,num2 = map(int,input("Enter Two diffrent Numbers: ").split())
if num1>num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)
