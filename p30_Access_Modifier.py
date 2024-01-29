'''
=========================================================================================
==================================Access Modifiers=========================================
=========================================================================================
Access Modifier in Object Oriented Programming is refers to the data security and data hiding.
-> Public
-> Private
-> Protected
'''



'''
===================================================================================
_____________________________Public Access Specifier____________________________
===================================================================================
'''
class Teacher():
    def __init__(self):
        print("\n--> This is Public Access specifier")

    # Public Variable
        self.name="Yash"

    # Public method
    def funName(self):
        return "Hello world"

a=Teacher()

print(a.name)
print(a.funName())





'''
===================================================================================
_____________________________Private Access Specifier____________________________
===================================================================================
'''
class person():
    def __init__(self):
        print("\n--> This is Private Access specifier")

    # Private variable
        self.__name="Yash"

    # Private method
    def __funName(self):
        return "Hello world"

a1=person()

print(a1._person__name)
print(a1._person__funName())


'''
===================================================================================
_____________________________Protected Access Specifier____________________________
===================================================================================
'''
class student():
    def __init__(self):
        print("\n--> This is Protected Access specifier")

    # Protected Variable
        self._name="Yash"

    # Protected Method
    def _funName(self):
        return "Hello world"

class subject(student):
    pass

a=student()
b=subject()

print(a._name)
print(a._funName())


print(b._name)
print(b._funName())
