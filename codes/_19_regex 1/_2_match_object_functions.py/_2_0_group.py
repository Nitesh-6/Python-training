"""
group() - Return the string matched by the RE
"""

import re


pattern = re.compile(r'\d+')
m1 = pattern.search('1234string')
print(f'm1 : {m1}')

result = m1.group()
print(f'group() : {result} ')
