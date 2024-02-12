"""
sub()   - Find all substrings where the RE matches, and replace them with a different string
"""


import re

p = re.compile('(blue|white|red)')

# blue , white or red will be replaced by colour
rep = p.sub('colour', 'blue socks and red shoes')
print(rep)

# here it will only replace one time
rep1 = p.sub('colour', 'blue socks and red shoes', count=1)
print(rep1)

# colour socks and colour shoes
# colour socks and red shoes