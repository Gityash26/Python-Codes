'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
================================ Generators In Python =================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-> Suppose we wants a list of all the even numbers from 1 to 100.
   Now the first way is to create a loop with some calculation and store all the even numbers 
   into a list or tuple and at the time of requirement we can access each value.

-> But all the values acquire some memory block that's why Generators are special type of function 
   that returns a generator object and we can generate value at the time of requirement.

-> The main benefit of using generator is to save memory and instead of storing each values we can 
   generate them just by using an object.

-> Generator is a very powerfull tool when we are dealing we larger data and complex computations.
   Therefore instead of generate all the values at once the generators helps to yield(produce) only 
   one and next when you required.
'''


def myGenerator():
    for i in range(50):
        yield i

g=myGenerator()

for j in g:
    print(next(g))