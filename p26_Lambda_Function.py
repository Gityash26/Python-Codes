'''
_________________________________________________________________________________________________
===================================== Lambda Function======================================
=================================================================================================
A lambda() is a function without a having any name. It basically often used where we require a small function for a short period of time.
It defined using the 'lambda' keyword.

syntax: 
        lambda argument : expressions



note : You are curious to know why would i use those lambda function approach for just a small calculation, Instead I can create a new variable and just store the calculated value.

But remeber functions only required memory when they were called So, lambda functions are generally used to provide as an arguments to higher order functions, such as map, filter, and reduce
'''


# This is a normal function
def add(a, b):
    print(f"Sum of {a} + {b} : {a+b}")


# This is lambda functions
f1 = lambda : "Hello world"

f2 = lambda x,y : x+y

f3 = lambda x, y : x-y

f4 = lambda x, y: (x*y)+30


print(f1())
print(f2(10,20))
print(f3(5,7))
print(f4(5,10))



# Sending lambda function as an arguments (Mostly Used for this purpose)
def greet(fx):
    return "Hello : "+fx()

print(greet(f1))




f=lambda: print("Hey! I am anonymous function (No Name) ")
f()
