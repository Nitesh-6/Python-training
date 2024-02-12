"""

Groups are numbered starting with 0. Group 0 is always present;
it’s the whole RE, so match object methods all have group 0 as their default argument.

"""

import re

# (username)@gmail.com
p = re.compile('(a(b)c)d') # group(0) = abcd , group(1) = abc, group(2) = b

m = p.match('abcd')

g = m.group(0)
print(g)

g1 = m.group(1)
print(g1)

g2 = m.group(2)
print(g2)

custom_g = m.group(2, 1, 2)
print(custom_g)
