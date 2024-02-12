"""
$ - Matches at the end of a line, which is defined as either the end of the string, or any location followed by a newline character.
"""

import re

print('=================case 1 : $ metacharacter =================')
pattern = re.compile(r'.o$')  # pattern matches string which ends with o
m1 = pattern.match('go')
print(f'm1 : {m1}')
