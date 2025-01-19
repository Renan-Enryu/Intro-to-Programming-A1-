# Make a list of your favorite fruits, and then write a series of independent if statements that check 
# for certain fruits in your list.
# •Make a list of your three favorite fruits and call it favorite_fruits.
# •Write five if statements. Each should check whether a certain kind of fruit is in your list.
# If the fruit is in your list, the if block 
# should print a statement,such as You really like bananas!


fruits = ['peach', 'banana', 'strawberry', 'mango', 'orange']

if 'mango' in fruits:
    print("That fruit is in your list.")
if 'banana' in fruits:
    print("That fruit is in your list.")
if 'strawberry' in fruits:
    print("That fruit is in your list.")
if 'orange' in fruits:
    print("That fruit is in your list.")
if 'peach' in fruits:
    print("That fruit is in your list.")

favorite_fruits = ['mango', 'banana', 'orange']

if 'mango' in favorite_fruits:
    print("\nWow you really love mangoes.")
if 'banana' in favorite_fruits:
    print("Wow you also like bananas.")
if 'strawberry' in favorite_fruits:
    print("That fruit is not in your list.")
if 'orange' in favorite_fruits:
    print("Orange is a really good fruit.")
if 'peach' in favorite_fruits:
    print("That fruit is not in your list.")