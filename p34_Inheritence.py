'''
=================================================================================================
=========================================Inheritence In Python===================================
=================================================================================================
Inheritence: 
In inheritence w can create a class with the halp of another class futher with some more properties.
If one class properties are common in another class then with te help of inheritence we can inherit their property.

   ______________                ________________
  |Parent class | ==========>   | Child class   |
 |_____________|               |_______________|
  


syntax :

class parent():
   pass
   

class Derived(parent):
     pass


=================================================================================================
=========================================Types of Inheritence====================================
=================================================================================================
(1)-> Single Inheritence
(2)-> Multilevel Inheritence
(3)-> Multiple Inheritence
(4)-> Hierarchical Inheritence
(5)-> Hybrid Inheritence



Important note:   
super().function_name()   : It is called Function Overriding
                            it is used to call same name function of parent class into child class 

'''


'''
-> (1)Single Inheritence : 
    ______________
   |__Employee___|
         |
         |
    _____|________
   |_____Car_____|

'''


class Employee():
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id

    def display(self):
        print(f"\nEmployee Name : {self.name} and Employee Id : {self.Id}")


class programmer(Employee):
    def __init__(self, name, Id, lan="Python"):
        super().__init__(name, Id)
        self.language = lan

    def display_Programmer(self):
        super().display()
        print(f"The Programmer Language : {self.language}")


p = programmer("Yash", 77, "JAVA")
p.display()


'''
-> (2)Multiple Inheritence : 
    ______________               _______________
   |____person___|              |____dance_____|
         |                             |
         |_____________________________|                             
                        |
                ________|________
               |_____Dancer_____|
'''


class person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("\nName of the Person:", self.name)


class Dance:
    def __init__(self, danceType):
        self.danceType = danceType

    def display(self):
        print("\nDanceType :", self.danceType)


class DancerPerson(person, Dance):
    def __init__(self, name, danceType):
        super().__init__(name)
        Dance.__init__(self, danceType)

    def display(self):
        super().display()
        Dance.display(self)


dancer1 = DancerPerson("Sneha", "Hip Hop")
dancer1.display()


'''
-> (3)MultiLevel Inheritence : 
    _________________            
   |_grandParent____|             
         |                    
    _____|________            
   |___Parent____|             
         |                    
    _____|________              
   |___Child_____|             
   
'''


class Grandparent:
    def greet(self):
        print("Hello from Grandparent!")


class Parent(Grandparent):
    def introduce(self):
        print("I am the Parent.")


class Child(Parent):
    def display(self):
        print("I am the Child.")


# Create objects and test
child_obj = Child()
child_obj.greet()      # Call method from Grandparent
child_obj.introduce()  # Call method from Parent
child_obj.display()    # Call method from Child


'''
-> (4)Hybrid Inheritence : 
   When we use more than one inheritence then it is called hybrid inheritence.
    ___________________      _____________________      
   |__Base class 1____|     |___Base class 2_____|              
         |___________________________|
                   _____|________            
                  |___Parent____|             
                        |                    
                   _____|________              
                  |___Child_____|             
   
ex: Multiple and multilevel
'''


