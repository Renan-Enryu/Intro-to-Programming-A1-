# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
# age, and then tell them the cost of their movie ticket

Age = int(input("Welcome To The Movie Theater, Enter your Age: "))
print("Age Entered:", Age)
if Age < 3:
        print("Your Movie Ticket is Free.")
elif 3 < Age <= 12:
        print("Your Movie Ticket costs $10.")
elif Age > 12:
        print("Your Movie Ticket costs $15.")
