"""                                    Decorators

- Decorators are evolved from the concept of closures.
- A decorator function is a higher order function that takes a function as an argument and returns the inner function.
- A decorator is capable of adding extra functionality to an existing function, without altering it.
- The decorator function is prefixed with @ symbol and written above the function definition.



"""
# Example

@outer
def greet():
    pass


"""

Consider the following three examples:
-First one shows the creation of closure function wish using the higher order function outer.
-The second one shows the creation of decorator function outer, which is used to decorate function greet. This is achieved with a small change to Example1.
-Third one displays decorating the greet function with decorator function, outer, using @ symbol.

"""


# Example 1

def outer(func):
    def inner():
        print("Accessing :", 
                  func.__name__)
        return func()
    return inner
def greet():
   print('Hello!')
wish = outer(greet)
wish()

"""
- wish is the closure function obtained by calling an outer function with the argument greet.
- When wish function is called, inner function gets executed.
Output
Accessing : greet
Hello!

"""

# Example 2

def outer(func):
    def inner():
        print("Accessing :",func.__name__)
        return func()
    return inner

def greet():
   return 'Hello!'

greet = outer(greet) # decorating 'greet'
greet()  # calling new 'greet'

# Output
Accessing : greet

"""
- The function returned by outer is assigned to greet i.e the function name passed as argument to outer.
- This makes outer a decorator to greet.

"""


"""

- In Python, decorating a function can also be achieved by writing decorator function name, prefixed with @ symbol, just above the function to be decorated.
- Hence, greet = outer(greet) expression is same as @outer.

"""
# Example 3

def outer(func):
    def inner():
        print("Accessing :",func.__name__)
        return func()
    return inner
@outer
def greet():
    return 'Hello!'
greet()

# Output
# Accessing : greet
