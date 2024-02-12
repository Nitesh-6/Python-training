"""
| - (or)  If A and B are regular expressions, A|B will match any string that matches either A or B.
        ex := Crow|Servo will match either 'Crow' or 'Servo', not 'Cro', a 'w' or an 'S', and 'ervo'.
"""

import re


pattern = re.compile('crow|sparrow')
m = pattern.match('crow')
print(m)

m1 = pattern.match('sparrow')
print(m)

m2 = pattern.match('cuckoo')
print(m)
