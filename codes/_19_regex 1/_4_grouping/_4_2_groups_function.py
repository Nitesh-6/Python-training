"""
The groups() method returns a tuple containing the strings for all the subgroups,
from 1 up to however many there are.
"""

import re

p = re.compile('(a(b)c)d')

m = p.match('abcd')

gs = m.groups() # inside the string how many matched
print(gs)
