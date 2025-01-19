# Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

# Answer = "Continue" 
# while Answer == "Continue":
#     PizzaT = input("Enter a Pizza Topping:")
#     print("adding",PizzaT,'..')
#     Answer = input("Enter more toppings?(Continue): ")

Answer = ""
while Answer != "Quit":
    PizzaT = input("Enter a Pizza Topping: ")
    print("Now adding", PizzaT, "to your Pizza")
    Answer = input("Enter more toppings? (Type 'Continue' to add more or 'Quit' to stop): ")
    if Answer == "Continue":
        continue
    elif Answer == "Quit":
        break