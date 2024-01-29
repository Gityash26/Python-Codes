'''
_________________________________________________________________________________________________
=====================================Map, Filter and  Redeuce======================================
=================================================================================================
-> MAP, filter, reduce not only present in python it is also in other languages also.
-> They can be applied to other sequences also



_________________________________________________________________________________________________
==========================================Map in Python==========================================
=================================================================================================
=> The map function applies any function to each element of a sequence and returns a new sequence cotaining the transformed sequence.
=> It is a higher order function
syntax : 
           map( function , iterable)
'''

# For example :
# Ques: We have a list and we wants to make square of each element in that list




def square(value):
    return value**2


# Applying normal method 
# =================================================================================================
l=[2,4,6,8,10]
newl=[]
for i in l:
    newl.append(square(i))

print(newl)
# =================================================================================================



# Applying map-function() 
# =================================================================================================
A=[1,2,3,4,5,6]
new_A=[]
new_A=list(map(square,A))
print(new_A)
# =================================================================================================




'''
_________________________________________________________________________________________________
==========================================Filter in Python==========================================
=================================================================================================
The filter function filters a sequence of elements basd on a given function (that returns a boolean value) and return a new sequence.  
=> It Helps to extract elements from a sequence on the basis of some condition
=> It is a higher order function
'''
def FilterFunction(num):
    return num>5


# Applying filter-function() 
# =================================================================================================
mylist=[1,3,5,7,9,11,23]

new_Mylist=list(filter(FilterFunction,mylist))

print(new_Mylist)
# =================================================================================================








'''
_________________________________________________________________________________________________
==========================================Reduce in Python=======================================
=================================================================================================
=> It is a higher order function
=> We require to import reduce
'''

from functools import reduce

num=[1,2,3,4,5]

def mysum(x,y):
    return x+y

sum=reduce(lambda x,y : x+y,num)
# sum=reduce(mysum,num)
print(sum)











# Example of using map, filter, and reduce in Python  
data = [1, 2, 3, 4, 5]  
  
# Using the map to apply a function to each element  
# Lambda function returns the square of x  

result1 = map(lambda x: x * 2, data)  # Result: [2, 4, 6, 8, 10]  
  
# Using the filter to filter elements based on a condition  
# Lambda function returns True for an even number  

result2 = filter(lambda x: x % 2 == 0, data)  # Result: [2, 4]  
  
# Using reduce to aggregate elements  
# Lambda function returns product of x and y  

from functools import reduce  
result3 = reduce(lambda x, y: x * y, data)  # Result: 120  