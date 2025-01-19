# Now that you know how to loop through a dictionary, 
# clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms 
# to your glossary.When you run your program again, these new words 
# and meanings should automatically be included in the output.

Dict = {'Concatenate:': '\n Link (things) together in a chain or series.', 
'Sorting:': '\n Arrange systematically in groups; separate according to type.',
'String:': '\n Used for representing textual data.',
'Syntax:': '\n Set of rules that defines how a Python program will be written and interpreted.',
'Variable:': '\n Reserved memory location to store values.',
'Integer:': '\n Used for representing numerical data',
'Loop:': '\n Control structure in Python that repeatedly executes a block of code as long as a given condition is true.',
'Class:': '\n Classes can be considered as a blueprint for objects.',
'Dictionary:': '\n A mutable, unordered collection of key-value pairs.',
'Function:': '\n A block of organized, reusable code used to perform a single, related action.'}

for x, y in Dict.items():
  print(x, y)
