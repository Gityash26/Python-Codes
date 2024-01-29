'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
=======================Function Caching in python=========================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-> Function Caching is a technique used for improving the performance of a program by storing 
   the results of a function call so that you can reuse the results instead of computing them 
   every time the function is called.

-> This can be useful when function is computationally expensive or when the inputs for the 
   fuction are same for a while for frequently .
  

'''
from functools import lru_cache
import time


@lru_cache(maxsize=None)                # Memoize
def delay_Display(n):
    time.sleep(5)
    return n*5


print("\nDisplaying With sleep :::\n")

print(delay_Display(10))
print("Done for 10")

print(delay_Display(20))
print("Done for 20")

print(delay_Display(30))
print("Done for 30")

'''
The function calls executed for 10,20 and 30, So their results are already stored in the cache.
In this example we try to again call same function for those values, Therefore instead of again call that function interpreter provide us cache stored value. 
'''

print(delay_Display(10))
print("Done for 10")

print(delay_Display(20))
print("Done for 50")

print(delay_Display(30))
print("Done for 60")


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Note: When to use function Caching:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When we have a functio with expensive computational and we sure about the imput values repeats So, 
Instead of compute those values we can store their results into cache.



'''
