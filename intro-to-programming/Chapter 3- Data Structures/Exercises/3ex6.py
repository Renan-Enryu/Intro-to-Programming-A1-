# You just found out that your new dinner table 
# won’t arrive in time for the dinner, and you have space for only two guests.
# •Start with your program from Exercise 3-5. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time 
# until only two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# •Print a message to each of the two people still on your list, letting them know they’re still invited.
# •Use del to remove the last two names from your list, 
# so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

people = ["Uryu", "Aizen", "Yhwach"]

print("New Message:\n Unfortunately due to a misunderstanding we can only seat 2 people for dinner,\n Apologies for the inconvenience.")
people.pop(0) 

print("\nI am sorry Uryu having the changes made, you have been removed from the list.")

print("Howewver",people[0],"and",people[1],"are still invited and are still welcome to join the dinner.")

del people[0]
del people[0]

print("\n",people,"\r")