'''
D Drive
--------
folders    Books
                - C
                - Java
                - Python
           onlinematerial
           Movies
                - English
                - Hindi
                - Telugu
           songs
           scanned copies
           Python Programs
           Photos
'''
'''
Windows       ==>   Folder       File
Linux         ==>   Directory    File 
P.L Python    ==>   Package*     Module*

Folder : All sub folders / 
         All files /
         combination of Folders and Files 
         
Package :   I.  all Sub Packages / 
           II.  all Modules /
          III.  combination of Sub Packages and Modules 
          Example: 
            _12_OOPs                    :  I. all sub packages
            _0_maths_basics            :  II. collection of all modules 
            _04_Operators               : III. combination of sub packages and modules
    
Module : .py file is a module
         Collection of Variables, 
                       Functions and 
                       Classes
          
'''
x = 10
print("Value : ", x)

print("Id type : ", id(x), type(x))


'''
builtins.py       - default module available

#include<stdio.h>  <==>   import builtins      import java.lang.io
void main():                   print()          System.out.println("Hello World")
    printf()                   type()
    scanf()                    id()


'''
# from builtins import print, input, len, max, min, print, sorted, sum
print(10)
print("----Builtin function calls-----")
val = input("Enter any number")
print(val)
len()
max()
min()
print()
sorted()
sum()
