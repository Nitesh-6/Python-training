"""
split() - Split the string into a list, splitting it wherever the RE matches
"""

import re
p = re.compile(r'\W+')

lt = p.split('This is a test, short and sweet, of split()')
print("lt = ", lt)

# 3 represents it should only be split 3 times
lt1 = p.split('This is a test, short and sweet, of split()', 3)
print("lt1 = ",lt1)

st = 'This  is a test, short and sweet, of split()'
print(st.split())
