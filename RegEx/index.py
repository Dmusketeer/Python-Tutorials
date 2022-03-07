"""
                          Regular Expressions

Regular expressions are patterns that help in filtering the text possessing them, and also in extracting portions of data that match the patterns, for further use.

The patterns are built using special characters.

Python uses re package to deal with regular expressions.


"""


import re
text="information"
pattern = "for"
if re.search(pattern, text):
    print(f"'{text}' contain {pattern}")