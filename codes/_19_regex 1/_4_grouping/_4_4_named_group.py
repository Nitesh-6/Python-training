"""
Named group (?P<name>...):  Named groups behave exactly like capturing groups,
and additionally associate a name with a group.

The match object methods that deal with capturing groups all accept either integers that refer
to the group by number or strings that contain the desired group’s name.
Named groups are still given numbers, so you can retrieve information about a group in two ways:
"""

import re

p = re.compile(r'(?P<word>\b\w+\b)')

m = p.search('(((( Lots of punctuation )))')

g = m.group('word')
print(g)

g1 = m.group(1)
print(g1)

m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')

di = m.groupdict()
print(di)
