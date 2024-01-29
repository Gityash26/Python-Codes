'''
_________________________________________________________________________________________________
===================================== seek() and tell()======================================
=================================================================================================
seek() and tell() functions in python are used to control a cursor around in a file so that we can edit t specific position.

 seek() : used to move cursor to a specific position
 tell() : It shows the cursor position 
'''

with open("abc.txt","r") as f:

# Moving cursor to 3th position
    f.seek(3)
    print(f"\nCurrent Position : {f.tell()}")

# Reading next 5 characters
    print(f"\nYour characters : {f.read(5)}")
    f.truncate(10)




