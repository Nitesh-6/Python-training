"""
1. [] - (character class) They’re used for specifying a character class,
       which is a set of characters that you wish to match

        ex := 
        ex1) [abc] will match any of the characters 'a','b', or 'c' 
        ex2) [a-c] is same but uses a range to represent set of characters to match 
        ex3) [a-z] from any of the characters from 'a' to 'z'
        ex4) [1-99] for any of 1 to 99
        ex5) [a-zA-Z0-9_] matches any alphanumeric character

"""

import re


# creating a pattern
pattern = re.compile(r'[A-Za-z]')

# checking whether the pattern matches given string(giv_str)
#  using pattern.match(giv_str)
m1 = pattern.match('a')     # this is a match object
m2 = pattern.match('b')     # this is a match object
m4 = pattern.match('d')

# printing match object(it shows the span range it matched with respect to index and what it matched)

print(m1)
# output:=  <re.Match object; span=(0, 1), match='a'>

# to check what it matched in the given string we use group() method of match object
print(m1.group())


print(m4)  # returns none as the given string didnt match the characters present in character class


print('----------------------------------------------')

print(' the character class using range ')

pattern1 = re.compile(r'[a-c]')  # same as above pattern


m1 = pattern.match('a')     # this is a match object
m3 = pattern.match('d')


print(m1)
# output:=  <re.Match object; span=(0, 1), match='a'>

print('the match object m1 is: ', m1.group())

print('the match object m4 is: ', m4)


print('-----------------------------------------')
print('character class containing 2 or more ranges')

# this matches any character from a to z and A to Z not other than that
pattern2 = re.compile(r'[a-zA-Z]')

m1 = pattern2.match('Y')  # this will match
m2 = pattern2.match('h')  # this will also match
m3 = pattern2.match('1')  # this will not match

print(m1)
print(m3)

# different types of patterns
# this matches all alphanumeric characters
pattern3 = re.compile(r'[a-zA-z0-9]')
