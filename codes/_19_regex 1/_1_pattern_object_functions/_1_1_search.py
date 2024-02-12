"""
search() - Scan through a string, looking for any location where this RE matches.
"""

import re


pattern = re.compile(r'are')
# search finds the match anywhere in the string but match only matches from the beginning of the string
m1 = pattern.search('who are you? are you fine')
if m1:
    print("your logic")
else:
    print("another logic for not matching")
print(m1)

# <re.Match object; span=(4, 7), match='are'>