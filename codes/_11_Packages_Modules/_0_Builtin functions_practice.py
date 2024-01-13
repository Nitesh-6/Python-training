'''
Reference : https://www.pythoncheatsheet.org/cheatsheet/built-in-functions
# include<stdio.h>
'''
print("Hello World")
print("Hello World", 10, 20, 30, 40, 50)

'''
Builtin Functions:
-------------------
builtins.py  1 Hour:
========================
Function	Description
--------------------------------------------------------------------
id()	Return the “identity” of an object.
input()	This function takes an input and converts it into a string.

print()	Print objects to the text stream file.
type()	Return the type of an object.

int()	Return an integer object constructed from a number or string.
float()	Return a floating point number from a number or string.
bool()	Return a Boolean value.
chr()*    	Return the string representing a character.
str()	Return a str version of object.
list()	Rather than being a function, list is a mutable sequence type.
tuple()	Rather than being a function, is actually an immutable sequence type.
dict()	    Create a new dictionary.
set()	Return a new set object.
frozenset()* Return a new frozenset object.

len()	Return the length (the number of items) of an object.
max()	Return the largest item in an iterable.
min()	Return the smallest item in an iterable.

ascii()* 	Return a string with a printable representation of an object.
bin() *	Convert an integer number to a binary string.


map()    *	Return an iterator that applies function to every item of iterable.
filter() *	Construct an iterator from an iterable and returns true.
reduce() *  (not builtin function)

ord()   *	Return an integer representing the Unicode code point of a character.
sorted()*	Return a new sorted list from the items in iterable.
zip()  **  Iterate over several iterables in parallel.
sum()	   Sums start and the items of an iterable.
any() *	Return True if any element of the iterable is true.
all() *	Return True if all elements of the iterable are true.
dir() * 	Return the list of names in the current local scope.
eval()	*   Evaluates and executes an expression.
exec()	*    This function supports dynamic execution of Python code.
isinstance() *	Return True if the object argument is an instance of an object.
issubclass() *	Return True if class is a subclass of classinfo.
iter()*	Return an iterator object.
next()*	Retrieve the next item from the iterator.

abs() *	Return the absolute value of a number.
enumerate()* Return an enumerate object.
hash()*	Return the hash value of the object.
help() *	Invoke the built-in help system.

OOPS
setattr()*	This is the counterpart of getattr().
hasattr()*	True if the string is the name of one of the object’s attributes.
delattr()*	Deletes the named attribute, provided the object allows it.
getattr()*	Return the value of the named attribute of object.
repr()*	Return a string containing a printable representation of an object.

FileHandling
open()*	Open file and return a corresponding file object.
enter()*
exit()*

Knowledge: Read: 1 Hour:
----------------------
aiter()	Return an asynchronous iterator for an asynchronous iterable.
breakpoint()	Drops you into the debugger at the call site.
bytearray()	Return a new array of bytes.
bytes()	Return a new “bytes” object.
callable()	Return True if the object argument is callable, False if not.
classmethod()	Transform a method into a class method.
compile()	Compile the source into a code or AST object.
complex()	Return a complex number with the value real + imag*1j.
divmod()	Return a pair of numbers consisting of their quotient and remainder.
format()	Convert a value to a “formatted” representation.
globals()	Return the dictionary implementing the current module namespace.
hex()	Convert an integer number to a lowercase hexadecimal string.
locals()	Update and return a dictionary with the current local symbol table.
object()	Return a new featureless object.
oct()	Convert an integer number to an octal string.
pow()	Return base to the power exp.
property()	Return a property attribute.
reversed()	Return a reverse iterator.
round()	Return number rounded to ndigits precision after the decimal point.
slice()	Return a sliced object representing a set of indices.
staticmethod()	Transform a method into a static method.
super()	Return a proxy object that delegates method calls to a parent or sibling.
vars()	Return the dict attribute for any other object with a dict attribute.
import()	This function is invoked by the import statement.

Exception Handling **:
--------------------
BaseException
Exception
All Errors
    ArithmeticError
    AttributeError
    KeyError
    NameError
    TypeError


Iterator **: 
-------------
iter() next()  
StopIteration

File Handling **:
------------------
open()
enter()
exit()

'''