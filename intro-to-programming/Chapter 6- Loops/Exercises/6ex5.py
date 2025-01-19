# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['Cheese', 'Pastrami', 'Chicken', 'Turkey', 'Pastrami', 'Egg', 'Ham', 'Pastrami']

finished_sandwiches = []

print('Sorry, the deli has run out of Pastrami.')

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches made:")
print(finished_sandwiches)