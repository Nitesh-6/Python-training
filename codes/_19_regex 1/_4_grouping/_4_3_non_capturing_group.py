"""
Non-capturing group (?:...) : Sometimes you’ll want to use a group to denote a part of a regular expression,
 but aren’t interested in retrieving the group’s contents

"""

import re

pattern = re.compile(f'([abc])+')
m = pattern.match('abc')
gs = m.groups()
print(gs)

pattern1 = re.compile(r'(?:[abc])+')
m1 = pattern1.match('abc')
gs1 = m1.groups()
print(gs1)


"""
Except for the fact that you can’t retrieve the contents of what the group matched, 
a non-capturing group behaves exactly the same as a capturing group; 
you can put anything inside it, repeat it with a repetition metacharacter such as *, 
and nest it within other groups (capturing or non-capturing)

"""
