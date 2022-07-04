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


## Python Class Variables

- Everything in Python is an object including a class
- When you define a class using the class keyword, Python creates an object with the name the same as the class’s name. For example:


```py
class MyFirstClass:
        pass
```

- This example defines the MyFirstClass class and the MyFirstClass object. The MyFirstClass object has the __name__ property:
```py
print(MyFirstClass.__name__) # MyFirstClass
```

- And the MyFirstClass has the type of type:

```py
print(type(MyFirstClass))  # <class 'type'>
```

- It’s also an instance of the type class:
```py
print(isinstance(MyFirstClass, type)) # True
```


- Class variables are bound to the class. They’re shared by all instances of that class.


```py
class MyFirstClass:
        Name="Dheeraj"
        classVersion=1

```

- Both Name and classVersion are class Variables of the MyFirstClass class .They are bound to the MyFristClass.


### Get the values of class variables

- To get the values of class variables, you use the dot notation (.). For example:

```py
print(MyFirstClass.Name) # Dheeraj
print(MyFirstClass.classVersion) # 1
```

- **If you access a class variable that doesn’t exist, you’ll get an AttributeError exception.**

- Another way to get the value of a class variable is to use the **getattr()** function. 

- The **getattr()** function accepts an object and a variable name. It returns the value of the class variable.

```py
name=getattr(MyFirstClass,"Name")
version=getattr(MyFirstClass,"classVersion")
print(name)
print(version)
```

- If the class variable doesn’t exist, you’ll also get an **AttributeError** exception. To avoid the exception, you can specify a default value if the class variable doesn’t exist like this:
```py
fName=getattr(MyFirstClass,"fName","text/html")
print(fName)
```

### Set values for class variables
- To set a value for a class variable, you use the dot notation:
```py
MyFirstClass.age=20
```
- or you can use the **setattr()** built-in function:

```py
setattr(MyFirstClass, 'age', 20)
```

### Delete class variables
- To delete a class variable at runtime, you use the **delattr()** function:
```py
delattr(MyFirstClass, 'age')
```
- Or you can use the del keyword:
```py
del HtmlDocument.version
```