'''
=========================================================================================
====================================Polymorphism in Python===============================
=========================================================================================
Polymorphism refers to their are same name functions but having multiple functionality according to the arguments given.
ex: len() can be used to find out length of a string, List, Tuple, Set etc

Their are two types of polymorphism in Python:
(1)-> Function Overloading
(2)-> Operator Overloading





====================================================================================================
-> Difference Between Function Overloading and Function Overriding
====================================================================================================


====================================================================================================
=> FUNCTION OVERLOADING
====================================================================================================

-> Methods or functions must have the same name and different signatures.	

-> Method overloading is a example of compile time polymorphism.	

-> Inheritance may or may not be required.	

-> Method overloading is performed between methods within the class.	

-> It is used in order to add more to the behavior of methods.	

-> In method overloading, there is no need of more than one class.	

-> There is No need of at least of two classes.


=> FUNCTION OVERRIDING
====================================================================================================

-> Method overriding is a example of run time polymorphism.

-> Inheritance always required.

-> Method overriding is done between parent class and child class methods.

-> It is used in order to change the behavior of exist methods.

-> There is need of at least of two classes.






====(1)-> Function Overloading===============================
=========================================================================================
Same name functions with different Arguments or parameters.
'''

print("\nUsing the Concept of Function Overloading : \n")


class Area:
    def findArea(self, a=None, b=None):
        if a != None and b != None:
            print(f"\n-> Area Of Rectangle : {a*b}")
        elif a != None:
            print(f"\n-> Area Of Square : {a*a}")
        else:
            print("-> Nothing To Find")


a = Area()
a.findArea()
a.findArea(10)
a.findArea(20, 30)


'''
====(2)-> Function Overriding===============================
=========================================================================================
Same name functions with same Arguments or parameters just call in the derived class.
'''

print("\nUsing the Concept of Function Overriding : \n")


class Base():
    def display(self):
        print("-> Hey I am Base Class")


class Derived(Base):
    def display(self):
        super().display()
        print("-> Hey I am Derived Class")


p = Derived()
p.display()


'''
====Another Example of Function Overriding===============================
=========================================================================================
Same name functions with same Arguments or parameters just call in the derived class.
'''


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class circle(shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return 3.14 * super().area()


rec = shape(10, 5)
print(f"\nArea of Rectangle : {rec.area()}")

c = circle(5)
print(f"\nArea of Circle : {c.area()}")


'''
==============================================================================================
======================================Operator Overloading====================================
==============================================================================================
-> Operator Overloading is a feature in python that allows developer to redefine mathemetical and comparision operators for  custom datatypes.

-> This means that we can use the standard mathematical operators (+, -, *, / etc) and comparision operators (<, >, == etc) in our own classes and use them just like other built in datatypes like int, float, and str.

--------------------------------------
=> WHY WE NEED OPERATOR OVERLOADING :
--------------------------------------
It helps to make the code more readable and concise.

'''
print("\nUsing the concept of Operator Overloading :\n")


class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i} i + {self.j} j + {self.k} k"

    def __add__(self, v):
        return vector(self.i+v.i, self.j+v.j, self.k+v.k)


v1 = vector(2, 5, 10)
v2 = vector(3, 4, 8)

print(v1)
print(v2)
print(v1+v2)




'''
========================================================================================
_________________________Mathematical Operators That Can Be Overload
========================================================================================
Addition	        :       p1 + p2	       ->    p1.__add__(p2)
Subtraction	        :       p1 - p2	       ->    p1.__sub__(p2)
Multiplication	    :       p1 * p2	       ->    p1.__mul__(p2)
Power	            :       p1 ** p2	   ->    p1.__pow__(p2)
Division	        :       p1 / p2	       ->    p1.__truediv__(p2)
Floor Division	    :       p1 // p2   	   ->    p1.__floordiv__(p2)
Remainder (modulou) :       p1 % p2	       ->    p1.__mod__(p2)
Bitwise Left Shift	:       p1 << p2	   ->    p1.__lshift__(p2)
Bitwise Right Shift	:       p1 >> p2	   ->    p1.__rshift__(p2)
Bitwise AND	        :       p1 & p2	       ->    p1.__and__(p2)
Bitwise OR	        :       p1 | p2	       ->    p1.__or__(p2)
Bitwise XOR	        :       p1 ^ p2	       ->    p1.__xor__(p2)
Bitwise NOT	        :       ~p1	           ->    p1.__invert__()







========================================================================================
_________________________Comaprision Conditional Operators That Can Be Overload
========================================================================================
Less than ('<')	                :       p1 < p2	     :      p1.__lt__(p2)
Less than or equal to ('<=')	:       p1 <= p2	 :      p1.__le__(p2)
Equal to ('==')	                :       p1 == p2	 :      p1.__eq__(p2)
Not equal to ('!=')	            :       p1 != p2	 :      p1.__ne__(p2)
Greater than ('>')	            :       p1 > p2	     :      p1.__gt__(p2)
Greater than or equal to ('>=') :	    p1 >= p2	 :      p1.__ge__(p2)
'''