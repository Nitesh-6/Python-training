"""
^ - (Matches at the beginning of lines.)
In MULTILINE mode, this also matches immediately after each newline within the string.
"""

import re

print('---------------case 1: ^ metacharacter ---------------------')
pattern = re.compile(r'^g')  # it matches at the beginning of line
m1 = pattern.match('go')
print(f'm1 : {m1}')
