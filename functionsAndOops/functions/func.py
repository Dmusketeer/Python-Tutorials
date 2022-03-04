                            

"""
                    # Functions

# A function is a piece of code, capable of performing a similar task repeatedly.
# It is defined using def keyword in python.
# Syntax of a function :
        def <function_name>(<parameter1>, <parameter2>, ...):
        'Function documentation'
        function_body
        return <value>         
# Parameters, return expression and documentation string are optional.

"""

def square(x):
    '''return square of a number'''
    return x*x
num=int(input("Enter a number : "))
print(f'square of {num} is : ',square(num))
