# -:-Python OOPs Concepts -:-     


- In Python, object-oriented Programming (OOPs) is a programming paradigm that uses classes and objects in programming. 
- It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.
- The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data. 

### <b>Main Concepts of Object-Oriented Programming (OOPs) </b>
- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance

## <b>Class</b> 
- A class is a collection of objects.
- A class contains the blueprints or the prototype from which the objects are being created. 
- It is a logical entity that contains some attributes and methods. 

<b> Some points on Python class: </b> <br/> 
- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute


Class Definition Syntax:

        class ClassName:
        # Statement-1
        .
        .
        .
        # Statement-N


Ex: <br/>

    class Dog:
        pass

# -:-Objects -:-

- The object is an entity that has a state and behavior associated with it.
- It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.

### An object consists of :

- State: It is represented by the attributes of an object. It also reflects the properties of an object.
- Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
- Identity: It gives a unique name to an object and enables one object to interact with other objects.

To understand the state, behavior, and identity let us take the example of the class dog (explained above). 

- The identity can be considered as the name of the dog.
State or Attributes can be considered as the breed, age, or color of the dog.
The behavior can be considered as to whether the dog is eating or sleeping.

Ex : <br />

    obj =Dog()

This will create an object named obj of the class Dog defined above.