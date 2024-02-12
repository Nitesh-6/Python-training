"""
Author : Govind 
Date   : 10-02-2024
"""

"""
Regular expressions(regex) are used for pattern matching within strings.

Uses:
=====


Pattern Matching: Regular expressions allow you to define patterns to search for within strings. 
----------------- This is useful for tasks like finding specific substrings, validating data formats, 
                  and extracting information from text.

Text Manipulation: Regex can be used for replacing, removing, or modifying specific parts of a string. 
------------------ It provides a powerful and flexible way to manipulate textual data.

Data Validation: Reex are used for validating user inputs or ensuring that data follows a specific format. 
---------------- For example, checking if an email address or phone number is well-formed.

Parsing and Extraction: Regex is commonly used for parsing and extracting information from structured or semi-structured data.
----------------------- This is particularly useful in data processing tasks.

"""

import re

phone_pattern = re.compile(r'\+{1}91-\d{10}')

phone_number = "+91-1234569781"
if phone_pattern.match(phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")
