'''
=====================================================================================================
__________________________Class_Methods_As_Alternative_Constructor___________________________________
=====================================================================================================

In Oops the term construtor refers to a special type of method that is automatically invokes with the creation of an object of a class.
The objective of constructor is to initilize the object attributes, in a class

sometimes we require to use class methods as alternative constructor when parameter comes in different formate.

'''


# --> This is use of a Normal constructor

class Employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=Employee("Yash",77)
print(e1.name)
print(e1.age)




# --> This is use of a Class methods as Alternative constructor
# In this program the class method derive values from formate and call constructor
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age


    @classmethod
    def fromstr(cls,string):
        string=string.split("-")
        return cls(string[0],string[1])
    
    def display(self):
        print(f"Good Morning {self.name} you are {self.age} Years old")


s1=Student("Yash",21)
s1.display()

s2=Student.fromstr("Sanjay-22")
s1.display()








'''
===================================================================================================
---------------------------------------------Another Example--------------------------------------
===================================================================================================
'''
from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Additional Constructor    
    @classmethod
    def from_DOB(cls, name, DOB):
        age = cls.calculate_age(DOB)
        return cls(name, age)
    
    @staticmethod
    def calculate_age(DOB):
        current_year = datetime.now().year
        birth_year = DOB.year
        age = current_year - birth_year
        return age
    
    def display(self):
        print(f"\nPerson Name : {self.name} and Age : {self.age}")


p1 = Person("Navikant", 23)
p1.display()
p2 = Person.from_DOB("Navikant", datetime(2002, 10, 13))
p2.display()


