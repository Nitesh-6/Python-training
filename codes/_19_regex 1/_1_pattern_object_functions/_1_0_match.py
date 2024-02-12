"""
match() - Determine if the RE matches at the beginning of the string.
"""

import re

pattern = re.compile(r'\d+')
m1 = pattern.match('123who')  # it matches it has string beginning with number
print(m1)

m2 = pattern.match('john_cena')  # it doesnt match
print(m2)

""" match starts matching from the beginning of the string 
it wouldn't match even if the pattern is present anywhere in the string other than at the beginning """

pattern = re.compile(r'who')
m2 = pattern.match('i am who is not known')
print(f'm2 : {m2}')
