"""
Now, let us understand what is a higher order function.

A Higher Order function is a function, which is capable of doing any one of the following things:

It can be functioned as a data and be assigned to a variable.

    It can accept any other function as an argument.

    It can return a function as its result.

    The ability to build Higher order functions, allows a programmer to create Closures, which in turn are used to create Decorators.

"""

# functioned as a data 

def greet(name):
    return f"Hey {name}!!!"

print(greet("Dheeraj"))

wish=greet # greet function is assigned to a variable wish;
print(wish("Prakhar"))

print(type(wish)) # function

print(greet("Ram"))




