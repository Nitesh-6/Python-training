"""
Most letters and characters will simply match themselves.
For example, the regular expression test will match the string test exactly.

metacharacters - that do not match themselves
                 Metacharacters add flexibility and power to the search and manipulation capabilities of regular expressions.
this are the metacharacters present in python
            . ^ $ * + ? { } [ ] \ | ( )

1. `.` (Dot)              : Matches any character except a newline.
                            It is a wildcard character.

2. `^` (Caret)            : Matches the start of a string.

3. `$` (Dollar)           : Matches the end of a string.

4. `*` (Asterisk)         : Matches zero or more occurrences of the preceding character or group.

5. `+` (Plus)             : Matches one or more occurrences of the preceding character or group.

6. `?` (Question Mark)    : Matches zero or one occurrence of the preceding character or group.
                            It makes the preceding character optional.

7. `{}` (Curly Braces)    : Used for specifying a specific number of occurrences.
                           `{n}` matches exactly n occurrences,
                           `{n,}` matches n or more occurrences,
                           `{n,m}` matches between n and m occurrences.

8. `[]` (Square Brackets) : Defines a character class.
                            It matches any single character within the brackets.

9. `\` (Backslash)        : Escapes a metacharacter, allowing it to be treated as a literal character.
                            For example, `\.` matches a literal dot.

10. `|` (Vertical Bar)    : Acts as a logical OR. It allows for the alternation of patterns.
                            For example, `cat|dog` matches either "cat" or "dog".

11. `()` (Parentheses)    : Creates a capturing group.
                            It is used to group elements together and capture the matched content.
            
pattern object
--------------

pattern = re.compile(r'any_pattern') # this is the pattern object 

match object
-----------

m = pattern.match('pattern_to_be_matched') # this is a match object


"""

