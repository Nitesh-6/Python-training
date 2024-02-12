"""
Another zero-width assertion is the lookahead assertion. Lookahead assertions are available in both positive and negative form, and look like this:

(?=...)

    Positive lookahead assertion. This succeeds if the contained regular expression, represented here by ..., successfully matches at the current location, and fails otherwise. But, once the contained expression has been tried, the matching engine doesn’t advance at all; the rest of the pattern is tried right where the assertion started.


(?!...)

    Negative lookahead assertion. This is the opposite of the positive assertion; it succeeds if the contained expression doesn’t match at the current position in the string.
"""

import re

# lookahead example
example = re.search(r'geeks(?=[a-z])', "geeksforgeeks")

# display output
print("Pattern:", example.group())
print("Pattern found from index:",
      example.start(), "to",
      example.end())


""" output :

Pattern: geeks
Pattern found from index: 0 to 5
"""

example = re.search(r'geeks(?=[a-z])',
                    "geeks123")

# output
print(example)

""" output :=
None
"""


# negative lookahead : opposite of positive lookahead


# positive lookahead
example1 = re.search('geeks(?=[a-z])',
                     'geeksforgeeks')
print('Positive Lookahead:', example1.group())

# negative lookahead
example2 = re.search('geeks(?![a-z])',
                     'geeks123')
print('Negative Lookahead:', example2.group())


"""
Positive Lookahead: geeks
Negative Lookahead: geeks
"""
