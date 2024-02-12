"""
subn()  - Does the same thing as sub(),
but returns the new string and the number of replacements
"""

import re


p = re.compile('(blue|white|red)')

repn = p.subn('colour', 'blue socks and red shoes')
print(repn)

repn = p.subn('colour', 'blue socks and red shoes', count=1)
print(repn)
