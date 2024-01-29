'''
_________________________________________________________________________________________________
================================Random Module Functions==========================================
=================================================================================================

randint(start , end)  : Provides random value between given starting and ending numbers (both included)

randrange(start , end) : Provide ranom value between starting number->(included) and end number->(not included)

choice() : Returns any random value from a list as argument

random() : Returns a random float value between 0 and 1

shuffle() : Take a sequence and return in a random sequence

uniform() : Return a random float value between given parameters
'''

import random as m



#Randint()____________________________________________________________________________________________________

print("\nRandint() Values between 10 to 20 : ")
for i in range(10):
    print(m.randint(10,20),end=" , ")
#_____________________________________________________________________________________________________________



#Randrange()__________________________________________________________________________________________________

print("\n\nRandrange() Values between 10 to 20 : ")
for i in range(10):
    print(m.randrange(10,20),end=" , ")
#_____________________________________________________________________________________________________________



#Choice()_____________________________________________________________________________________________________

print("\n\nChoice() Between List Values [11,22,33,44,55] :  ")
l=[11,22,33,44,55]
for i in range(10):
    print(m.choice(l),end=" , ")
#_____________________________________________________________________________________________________________



#random()_____________________________________________________________________________________________________
print(f"\n\nRandom float Value (0 to 1): {m.random()}")
#_____________________________________________________________________________________________________________




#shuffle()____________________________________________________________________________________________________

a=[10,15,20,25,30,35,40]
m.shuffle(a)
print(f"\nshuffle List : {a}")
#_____________________________________________________________________________________________________________




#uniform()____________________________________________________________________________________________________

print(f"\nUniform Float Value (2 to 5): {m.uniform(2,5)}")
#_____________________________________________________________________________________________________________






