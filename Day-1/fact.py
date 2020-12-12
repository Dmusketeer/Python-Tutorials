# Write a Function to find Factorial of given Number?
def fact(num):
    '''this this the newbie method '''
    if num==1 or num==0:
        return 1
    if num<0:
        return 'plzz enter a positive input'
    if num>1:
        return num*fact(num-1)
print(fact(5))
print(fact(-1))
print(fact(1))
print(fact(0))

# Method 2: 
def facto(num):
    result=1
    while(num>1):
        result=result*num
        num=num-1
    return result
print(facto(5))
print(facto(7))