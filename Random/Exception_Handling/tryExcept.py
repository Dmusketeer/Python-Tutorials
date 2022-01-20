# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.




# Exception Handling
# When an error(exception) occurs Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:


# name="Dheeraj"
# The try block will generate an exception, because name is not defined
try:
    print(name)
except:
    print("An Exception occurs!")

