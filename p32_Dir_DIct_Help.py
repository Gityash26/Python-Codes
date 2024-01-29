'''
===================================================================================================
____________________dir() Method___________________________________________________________________
===================================================================================================
dir() Function helps to return all the functions that can be applied on any object or variable

'''

a=[2,3,4,5,6,7]
print("\nPrinting dir() ::: ")
for methods in dir(a):
    print(methods,end=" , ")






'''
===================================================================================================
      __dict__ 
===================================================================================================
__dict__ keyword provides a dictionary representation of an object {attribute : Value}
'''


class person:
    def __init__(self,name,age):
        print("\n\nPrinting __dict__ ::: ")
        self.name=name
        self.age=age
    
p=person("John",22)
print(p.__dict__)







'''
===================================================================================================
     help() Method 
===================================================================================================
help() Method is used to get help documentation for an object, Including a discription of its attribute and methods.

'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

S=student("Sachin",21)
print(help(S))