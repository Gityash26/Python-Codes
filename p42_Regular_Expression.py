'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
========================== regular Expression ===================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-> A Regular Expressions (RegEx) is a special and powerful tool for working with strings
   and text data in python.

-> This tool allows us to match and manipulate strings based on patterns, making it easy 
   to perform complex string operations with just few lines of code
'''

import re

pattern = "core"

text = '''Its core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
Rather than building all of its functionality into its core, Python was designed to be highly extensible via modules. 
This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. 
Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.'''


match=re.search(pattern,text)
print(match)
