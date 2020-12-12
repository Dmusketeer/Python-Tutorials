def fun(x,y):  # x, y are called parameters
    '''sun of two numbers'''
    return x+y
print(fun())     # this will give an error
print(fun(x))    # give Type Error  # x wil called argument at the time of calling
print(fun(y))    # give Type Error  # x wil called argument at the time of calling

# Write a function to take number as input and print its square value

def sqr(x):
    '''Square of the given number'''
    return x**2 
print('square is :',sqr(3))
