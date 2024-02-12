"""
The final metacharacter in this section is "." .
It matches anything except a newline character.
 "." is often used where you want to match “any character”.
"""

import re

print('----------------case 1: "." metacharacter ---------------')
pattern = re.compile(r'.')  # the pattern matches any character
m1 = pattern.match('3')
print(f'm1 : {m1}')

m2 = pattern.match('a')
print(f'm2 : {m2}')

pattern1 = re.compile(r'.*')  # the pattern matches any string
m3 = pattern1.match('who@reY0u')
print(f'm3 : {m3}')
