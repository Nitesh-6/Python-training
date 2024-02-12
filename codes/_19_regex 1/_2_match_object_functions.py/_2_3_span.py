"""
span()  - Return a tuple containing the (start, end) positions of the match
"""


import re

pattern = re.compile(r'\d+')
m1 = pattern.search('who is 100?')
print(m1)


sp = m1.span()
print(f'the span of match is : {sp}')
