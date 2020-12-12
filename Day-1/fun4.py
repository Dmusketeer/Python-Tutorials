# There are 4 types are actual arguments are allowed in Python.
#     1) Positional Arguments
#     2) Keyword Arguments
#     3) Default Arguments
#     4) Variable Length Arguments

# 1) Positional Arguments:
def sub(a, b):
    print(a-b)
sub(100, 200)
sub(200, 100)

# 1:)The number of arguments and position of arguments must be matched. If we change the order then result may be  changed.
# 2:)If we change the number of arguments then we will get error.


# 2)Keyword Arguments:

def wish(name, lname):
    print("Hello", name, lname)
wish(name="Dheeraj", lname="Tiwari")
wish(lname="Tiwari", name="Dheeraj")



#     3) Default Arguments

def wish(name="Guest"):
    print("Hello", name, "Dheeraj")
wish("Dheeraj")
wish()   # If we are not passing any name then only default value will be considered.

# Note: After default arguments we should not take non default arguments.


def wish(name="Guest", msg="Good Morning"): #Valid
def wish(name, msg = "Good Morning"): #Valid
def wish(name="Guest", msg):  # Invalid   #SyntaxError: non-default argument follows default argument
