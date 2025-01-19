# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, 
# print everything you know about # each pet

pet1 = {'Owner': 'Ichigo', 'TAnimal': 'Lion'}

pet2 = {'Owner': 'Kenzo', 'TAnimal': 'Cat'}

pet3 = {'Owner': 'Aqul', 'TAnimal': 'Dog'}

All = [pet1, pet2, pet3]

for pet in All:
    print(f'Owner - {pet["Owner"]}')
    print(f'Animal - {pet["TAnimal"]}\n')