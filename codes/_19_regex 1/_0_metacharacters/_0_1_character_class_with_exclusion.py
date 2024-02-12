"""
^
-------


You can match the characters not listed within the class by complementing the set.
This is indicated by including a '^' as the first character of the class.
For example, [^5] will match any character except '5'.
If the caret appears elsewhere in a character class, it does not have special meaning.
For example: [5^] will match either a '5' or a '^'.

"""


import re
print(' case 1 : ^ at the beginning inside []')

pattern = re.compile(r'[^542]')

# this will not match as it is there in the character class
m1 = pattern.match('4')
m11 = pattern.match(('542'))
m2 = pattern.match('0')  # this will match as it is not in the character class

print(m11)
print(m1)
print(m2)


print('---------------------------')
print('Case 2: ^ not at the beginning inside []')

# this will match with any character that is there inside the square brackets
pattern1 = re.compile(r'[54^]')

# as ^ is not at the beginning so ^ is also considered as character not as metacharacter inside the character class

m1 = pattern1.match('^')  # this will match
m2 = pattern1.match('5')
m3 = pattern1.match('0')  # this will not match


print(m1)
print(m3)
