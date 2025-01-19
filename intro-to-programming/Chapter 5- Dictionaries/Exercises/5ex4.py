# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# * Use a loop to print the name of each river included in the dictionary.
# * Use a loop to print the name of each country included in the dictionary.

Dict = {"Amazon River": "Brazil", "Nile River": "Egypt", "Yangtze River": "China"}

print("Sentences about each River:\n")
for x, y in Dict.items():
    print(f'{x} is the river that runs through {y}')

print('\nThe name of each major river:\n')
for x in Dict.keys():
    print(x)

print('\nThe name of each country the rivers pass through:\n')
for y in Dict.values():
    print(y)
