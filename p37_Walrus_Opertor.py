'''
=========================================================================================
============================ Walrus operator in Python ==================================
=========================================================================================
-> The Walrus Operator is a new addition in python that allows to assign values to a variable 
   within an expression.

-> It is represented by ':=' syntax and can be used in variety of contexts including while loop 
   and if statements.

-> Walrus operator helps when we require a value multiple times in a loop but don't wants to repeat
   the calculation. 

for example:

-----------------------------------------------------
--> OLd approach     
        a=10
        print(a)
-----------------------------------------------------
--> Walrus Operator Approach
       print(a := 20)
-----------------------------------------------------







===========================================================================================
======================= Walrus Operator Example 1 =========================================
===========================================================================================
'''

print(f"\n{'~'*100}\nUsing Old Approach POP()\n{'~'*100}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

n = len(l)
while n > 0:
    print(f"Pop Value -> {l.pop()}")
    n = n-1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


print(f"\n{'~'*100}\nUsing Walrus Approach POP()\n{'~'*100}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while (m := len(l)) > 0:
    print(f"Pop Value -> {l.pop()}")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


'''
===========================================================================================
======================= Walrus Operator Example 2 =========================================
===========================================================================================
'''

# Example Using Without Walrus Operator
food = list()
while True:
    f = input("\nEnter your favourite food : ")
    if f == 'quit':
        break
    food.append(f)
print("\n----> ", food, "\n\n")


# Example Using Walrus Operator
Myfood = list()
while (f := input("\nEnter food you like : ")) != 'quit':
    Myfood.append(f)

print("\n----> ", Myfood,)
