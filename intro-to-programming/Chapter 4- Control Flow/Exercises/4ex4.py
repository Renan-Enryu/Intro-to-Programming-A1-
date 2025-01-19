# Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
# •If the person is less than 2 years old, print a message that the person is a baby.
# •If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# •If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# •If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# •If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# •If the person is age 65 or older, print a message that the person is an elder.

# Input Age in the parenthesis Below. V
age = int(18) 

if age < 2:
    print("You are a Baby.")
elif 2 <= age < 4: 
    print("You are a Toddler")
elif 4 <= age < 13:
    print("You are a Kid.")
elif 13 <= age < 20:
    print("You are a Teenager.")
elif 20 <= age < 65:
    print("You are an Adult.")
else:
    print("You are an Elder.")