'''
==================================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Shutil Module in Python ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
==================================================================================================

-> The Shutil module allows you to do high-level file operations on a file, such as copy, create, 
   and remote operations. 

-> This module aids in the automation of the copying and deleting of files and folders. 





==================================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Functions of Shutil Module ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
==================================================================================================

(1) shutil.copy(src , dst)
    -> This function copies the file of src(source) to new location by dst(destination).
    -> If the dst location is already exist, the original file will be overwritten. 
    ->The destination might be a file or a directory, but the source must be a file. 

(2) shutil.copy2(src , dst)
    -> This copy2 is almost similar to copy() function to copy srvc file to dst file or directory.
    -> But it preserves more metadata about the originl file, such as timestamp.

(3) shutil.copytree(src , dst)
    -> This function recursively copies the src 'directory' to new location specified in dst.
    -> If dst location already exist then th eoriginal file will get merged with it.

(4) shutil.move(src , dst)
    -> This function moves the file from the source(src) to new location dsitination(dst)
    -> It is more like renaming a file in most cases.

(5) shutil.rmtree(path)
    -> This function is used to delete entire directory.

    
'''






import shutil
import os

# shutil.copy("abc.txt" , "abc2.txt")

# shutil.copy2(r"C:\Users\pc\Downloads\pexels-veeterzy-39811.jpg" , r"C:\Users\pc\Downloads\Image2.jpg")

# shutil.copytree(r"C:\Users\pc\Desktop\SQL Files",r"C:\Users\pc\Desktop\SQL Files 2")

# shutil.move(r"C:\Users\pc\Pictures\Camera Roll\Moved file.jpg",r"C:\Users\pc\Pictures\Moved file.jpg")

# shutil.rmtree("C:\python playlist\New dir")


for i in range(5,14):

    shutil.copy("C:\TURBOC3\BIN\PROJECT\PROGRAM1.CPP" ,f"C:\TURBOC3\BIN\PROJECT\PROGRAM{i}.CPP")