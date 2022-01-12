class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def detials(self):
        print(f'My name is {self.name}')
        print(f"Id Number is {self.idnumber}")


class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        # invoking the __init__ of the parent class
        Person.__init__(self,name,idnumber)

    def details(self):
        print(f'name is {self.name}')
        print(f"Id is {self.idnumber}")
        print(f"My Post is {self.post}")


# create an instance from object
A = Employee("Dheeraj",7777,500000,"ASE")
# calling a function of the class Person using
# its instance

A.display()  
#it"ll modify the behaviour of parent class    
A.details()         
