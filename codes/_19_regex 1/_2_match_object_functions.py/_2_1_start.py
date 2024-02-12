"""
start() - Return the starting position of the match
"""

import re

pattern = re.compile(r'\d+')
m1 = pattern.search('who is 100?')
print(m1)

st = m1.start()
print(f'start position of match : {st}')
