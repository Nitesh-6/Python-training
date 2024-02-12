"""
findall() - Find all substrings where the RE matches, and returns them as a list.
"""

import re

pattern = re.compile(r'\d{1}_[a-zA-Z]*')
m1 = pattern.findall('names present are 1_rama , 2_hanuman, 3_trump')
print(m1)
