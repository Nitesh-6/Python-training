"""
Some of the special sequences beginning with '\'
represent predefined sets of characters that are often useful,
such as the set of digits, the set of letters, or the set of anything that isn't whitespace.

\d

    Matches any decimal digit; this is equivalent to the class [0-9].
----------
\D

    Matches any non-digit character; this is equivalent to the class [^0-9].
----------
\s

    Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
----------
\S

    Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
----------
\w

    Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
----------
\W

    Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
----------

"""

import re


print('----------Case 1: \d  matches any digit from 0-9----------------')
pattern = re.compile(r'\d')

m1 = pattern.match('3')  # it matches the pattern
print(f'm1 : {m1}')

m2 = pattern.match('d')  # it doesnt match the pattern as it is not a digit
print(f'm2 : {m2}')

# the pattern 0 or more characters which are digits
pattern1 = re.compile(r'\d*')
m3 = pattern1.match('3434')
print(f'm3 : {m3}')

# the pattern 1 or more characters which are digits
pattern2 = re.compile(r'\d+')
m4 = pattern2.match('354646')
print(f'm4 : {m4}')

pattern3 = re.compile(r'\d?')
m5 = pattern3.match('3454')
print(f'm5 : {m5}')

m6 = pattern3.match('sddf')
print(f'm6 : {m6}')


print('--------------------Case 2: \D doesnt match any digit -----------')

pattern = re.compile(r'\D')
m1 = pattern.match('5')  # it doesnt match the pattern as it is a digit
print(m1)

m2 = pattern.match('d')  # it matches the pattern as it is not a digit


"""
practice other sequences
"""
