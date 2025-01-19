# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# * Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary,and store their meanings as values.
# * Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, or print 
# the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

Dict = {'Concatenate': 'Concatenate:\n Link (things) together in a chain or series.', 
'Sorting': 'Sorting:\n Arrange systematically in groups; separate according to type.',
'String': 'String:\n Used for representing textual data.',
'Syntax': 'Syntax:\n Set of rules that defines how a Python program will be written and interpreted.',
'Variable': 'Variable:\n Reserved memory location to store values.'}

print(Dict['Concatenate'])
print(Dict['Sorting'])
print(Dict['String'])
print(Dict['Syntax'])
print(Dict['Variable'])  

