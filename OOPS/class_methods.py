class Dog:
    # class attribute
    attr1="Mammel"
    # instance attribute
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f'My name is {self.name}')


# Object instantiation
Rodger=Dog("Rodger")
Tommy=Dog("Tommy")

# accessing class methods
Rodger.speak()
Tommy.speak()