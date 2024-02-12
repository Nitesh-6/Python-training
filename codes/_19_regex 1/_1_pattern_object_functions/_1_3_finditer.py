"""
finditer() - Find all substrings where the RE matches, and returns them as an iterator.
"""

import re


pattern = re.compile(r'\d+')

iterator = pattern.finditer('12 drummers drumming, 11 ... 10 ...')

print(f'iterator : {iterator}')

for match in iterator:
    # print(match.span())
    print(match.group())


