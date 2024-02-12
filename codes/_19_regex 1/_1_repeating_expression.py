"""
Repeating things
--------------------


for repeating things there are metacharacters used:

1.  '*' -(0 or more times matched) * doesn’t match the literal character '*'; instead, it specifies that the previous character can be matched zero or more times, instead of exactly once.

2. '+' - (which matches 1 or more times) 
        ex := ca+t will match 'cat' (1 'a'), 'caaat' (3 'a's), but won’t match 'ct'

3. '?' -(matches either once or zero times)
        ex := home-?brew matches either 'homebrew' or 'home-brew'

4. '{m,n}' - (m and n are decimal integers) [ This quantifier means there must be at least m repetitions, and at most n] 
        ex := a/{1,3}b will match 'a/b', 'a//b', and 'a///b'. It won’t match 'ab', which has no slashes, or 'a////b', which has four.

    You can omit either m or n; in that case, a reasonable value is assumed for the missing value. Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity.
        ex := a/{2}b will only match 'a//b'.


{0,} is the same as *, {1,} is equivalent to +, and {0,1} is the same as ?. It’s better to use *, +, or ? when you can, simply because they’re shorter and easier to read.

"""


import re

print('=========================== Case 1: * metacharacter ========================')

pattern = re.compile(r's*')  # pattern matches 0 or multiple time character s
m1 = pattern.match('ssss')
print(m1)

pattern1 = re.compile(r'\d*')  # pattern matches 0 or multiple digit number
m2 = pattern1.match('23435')
print(m2)

m3 = pattern1.match(r'fa1')    # it matches even if there is no number
print(m3)

print('=================== case 2: + metacharacter ===================')

pattern1 = re.compile(r's+')
m1 = pattern1.match('ssss')  # it matches as it has atleast one 's'
print(m1)

# it doesnt match because it should atleast have one 's'
m1 = pattern1.match('fgh')
print(m1)

print('===================== case 3 : ? metacharacter =====================')

pattern = re.compile(r'p?')  # it matches 'p' 0 or 1 time
m1 = pattern.match('p')
print(m1)

m2 = pattern.match('d')
print(m2)


print('======================== case 4 : {m,n} metacharacter =============')

# matches p if it repeates 2 till almost 4 times
pattern = re.compile(r'p{2,4}')
m1 = pattern.match('ppp')
print(m1)

m2 = pattern.match('pppppp')
print(m2)
