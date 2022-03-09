"""
Now, let us understand what is a higher order function.

A Higher Order function is a function, which is capable of doing any one of the following things:

It can be functioned as a data and be assigned to a variable.

    It can accept any other function as an argument.

    It can return a function as its result.

    The ability to build Higher order functions, allows a programmer to create Closures, which in turn are used to create Decorators.

"""

#                       **** functioned as a data **** 

def greet(name):
    return f"Hey {name}!!!"

print(greet("Dheeraj"))

wish=greet # greet function is assigned to a variable wish;
print(wish("Prakhar"))

print(type(wish)) # function

print(greet("Ram"))


print("\n************************\n")




#                       **** functioned as an Arguments **** 

def greet(fname,lname):
    return f"Hey {fname} {lname}!!!"

def add(x, y):
    return x + y
def sub(x, y):
   return x - y
def prod(x, y):
    return x * y
def do(func,x,y):
    return func(x,y)

print(do(add,2,3)) # add as an argument

print(do(greet,"Dheeraj","Tiwari"))


print("\n************************\n")




#                       **** Returning a function **** 

def outer():
    def inner():
        s="Hello World!!! Returning a function"
        return s
    return inner()

print(outer())
print("\n************************\n")

# *** NOTE : You can observe from the output that the return value of 'outer' function is the return value of 'inner' function. 


def outer():
    def inner():
        s="Hello Dheeraj"
        return s
    return inner # Removed '()' to return 'inner' function itself

print(outer())

func=outer()
print(type(func))
print(func()) # calling inner function

# *** NOTE: Parenthesis after the inner function are removed so that the outer function returns inner function.