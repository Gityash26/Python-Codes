'''
==================================================================================================
_______________________________Dunder methods ( '__' Double Underscore Methods)
=================================================================================================
These are special methods that are also known as magical or dunder methods. 
These methods can define in classes and provide a powerful way to manipulate objects and their behaviours.
Dunder methods or magical methods are initilize with "__" double underscore on their surrounding

ex :  __init__()	     :     Initialize the attributes of the object
      __str__()	         :     Returns a string representation of the object
      __len__()	         :     Returns the length of the object
      __add__()	         :     Adds two objects
      __call__()	     :     Call objects of the class like a normal function
'''

class Employee:
    def __init__(self,name):
        self.name=name

    # Dunder method
    def __len__(self):
        return len(self.name)

    # Dunder method
    def __str__(self):
        return f"\nName of the Employee : {self.name} -> __str__"
    
    # Dunder method
    def __repr__(self):
        return f"\nName of the Employee : {self.name} -> __Repr__"
    
    # Dunder method
    def __call__(self):
        print("\nHe I am a Callable Mehod -> __Call__")

a=Employee("Harry")
print(str(a))
print(repr(a))
a()

print(f"\nLength : {len(a)}")
print(f"\nDictionary Formate : {a.__dict__}")