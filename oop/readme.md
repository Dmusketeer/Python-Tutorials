# <center>Objects<center />

- An object is a container that contains the state and methods.

- Before creating objects, you define a class first. And from the class, you can create one or more objects. The objects of a class are also called instances of a class.

# <center>Define a class<center />
To define a class in Python, you use the class keyword followed by the class name and a colon.

```py
class Person:
    pass
```

- By convention, you use capitalized names for classes in Python. If the class name contains multiple words, you use the CamelCase format like EmpDetails.

- To create an instance of a class, you use the class name with parentheses like this:

        person = Person()

- When printing out the person object, you’ll see its name and memory address:
        
        <__main__.Person object at 0x000001C46D1C47d8>

- The person object is an instance of the Person class. The isinstance() function returns True if an object is an instance of a class:
```py
print(isinstance(person, Person))  # True
```

- Everything in Python is an object, including classes.
- When you define the Person class, Python creates an object with the name Person. The Person object has attributes.
- The Person object has the type of type:

```py
print(type(Person))
# Output:
<class 'type'>
```
**NOTE**
- An object is container that contains state and behavior.
- A class is a blueprint for creating objects.
- In Python, a class is also an object, which is an instance of the type.

