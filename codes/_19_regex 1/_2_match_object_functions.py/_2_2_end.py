"""
end()  - Return the ending position of the match
"""


import re

pattern = re.compile(r'\d+')
m1 = pattern.search('who is 100?')
print(m1)

lt = m1.end()
print(f'end position of match : {lt}')
