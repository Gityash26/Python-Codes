'''
________________________Encapsulation________________________

Encapsulation refers to create our variable private and we don't access it directly with object.
Private Variable can be access only with the help of methods.

=========================================================================================
===========================Normal Getter and Setter====================-==================
=========================================================================================
'''
class Person:
    def __init__(self, name):
        self.__name = name

    # Getter method
    def get_name(self):
        return self.__name

    # Setter method
    def set_name(self, name):
        self.__name = name

person = Person("John")
print(person.get_name())  # Output: John

person.set_name("Jane")
print(person.get_name())  # Output: Jane





'''
=========================================================================================
========================@property(Getter)   &  @functionName.setter======================
=========================================================================================

This method helps to call getter and setter function as an object property
Instead of using as, obj.getter()   and     obj.setter(value)
   We using it as,   obj.num        and     obj.num=value                  
'''
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

person = Person("John")
print(person.name)  # Output: John

person.name = "Jane"
print(person.name)  # Output: Jane










