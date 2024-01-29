'''
_________________________________________________________________________________________________
=================================Object Oriented Programming=====================================
=================================================================================================

Object oriented programming pradigm is a way of prgramming on the basis of classes and objects.
Oops concept is a most effective way to create an effective, readble, and Manageble code.
Normal functional programming works on logic and concept but Oops concept are used to deals with 
real world entities.
The object is related to real-word entities such as book, house, pencil, etc. 





=================================================================================================
                                            Class : 
=================================================================================================
classes are like template for any object. for example a blank train reservation form that are common for every passenger. Any person that wants to reserve seat in the train they they just require the fill reservation form and submit it a the counter.

Any real life based entity having some attributes that describe their identity Ex- Name, Age, Id, or Price, etc.
Also some methods that are used for their functioning. Ex- A player in the game fight, Run, Jump, A car move forward, Stop etc.

Therefore A class having some 'Attributes' & 'Methods'.
=================================================================================================


_class_______________________
|                           |
| Attributes                |
|     a,b,c                 |             
|                           |
| Methods()                 |
|     statements            |     =============>  Object
|     statements            |
|                           |
|___________________________|



=================================================================================================
                                            Object : 
=================================================================================================

Class is just a template and object is class instance that is creates with the help of class name.
Each object having its own template (As designed) And its own attributes and method




=================================================================================================
                                           Methods
=================================================================================================
Mehods are the function of an object that are created to provide an Abstraction to a user

for ex- A car move after acceleration, Stops after applying breaks, Turn after rotating steering wheel etc.
        A computer with Graphical Interface And lots of functioning capabilities 
Therefore A normal user just require to use those built functionalities without worrying about the exact concept used behind that functionality.
Same with the methods In class An object having their attributes and various methods and at the end the user just create an object and use those functinality.
=================================================================================================







=================================================================================================
Their are four pillars of Object Oriented Programming ::
=================================================================================================

(1)Abstraction

   The Abstraction refers to the hiding of unneccessary detials and just shows the required information to the user.
   Oops provide the data abstraction so that their should be only neccessary information visible to users.
=================================================================================================

=================================================================================================
(2)Encapsulation

   Just like any capsule a data attributes and methods are combined into a class.
=================================================================================================


=================================================================================================
(3)Inheritence

The Oops provides the inheritence feature that says that instead of increasing the code size use the inheritence feature that is also seems into real life when a child having some identical properties from their parents such as height, eye color, hair color, face etc.

In Inheritence if one class having some common properties of another class with some other attributes or features then instead of writing same code againg just inherit one class into another with aditions.
=================================================================================================


=================================================================================================
(4)Polymorphism

   The polymorphism comprises of two words poly(Many) morphism(Forms) In simple words we can say that Oops provide the feature of polymorphism in which we can make any method or operator to perform multiple task as per the requirement.
   ex : A person can be husband, Son, Employee, Brother, Cousin, Friend At different situation                                           
=================================================================================================

'''

class Myinfo():

    def accept(self):
        self.name=input("Enter your Name : ")
        self.age=input("Enter your Age : ")

    def display(self):
        print(f"\nHello {self.name} , You are {self.age} years old")
    
p1=Myinfo()
p1.accept()
p1.display()







'''
=================================================================================================
====================================Constructor In Python========================================
=================================================================================================

Constructor is a special type of function in a class that automatically invoke after the cretion of an object of that class.
Constructor can be prmeterize also.
syntax : 
          def __init__():
            Statements1
            Statements2
            Statementsn
      
'''

class Person():
    def __init__(self):
        print("\nHey! I Am Constructor")

p=Person()



