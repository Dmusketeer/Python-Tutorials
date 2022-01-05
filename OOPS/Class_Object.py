class Dog:
    # class attibute
    attr1="Mammal"
    attr2="Mammal type"
    # instance attribute
    def __init__(self,name):
        self.name=name
    
# Driver code
# Object Instantiation
Rodger=Dog("Rodger")
Tommy=Dog("Tommy")

# Accessing class attributes
print(f'Rodger is a {Rodger.__class__.attr1}')
print(f'Tommy is also a {Tommy.__class__.attr2}')

# Accessing instance attributes
print(f"My Name is {Rodger.name}")
print(f"My Name is {Tommy.name}")

