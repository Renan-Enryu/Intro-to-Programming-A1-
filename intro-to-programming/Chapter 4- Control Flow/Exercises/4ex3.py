# Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed for the appropriate color alien.

# Input Color Here V
print("\nif Version-------------------------------------")
alien_color = ('Green') 

green_color = ('Green')
yellow_color = ('Yellow')
red_color = ('Red')

if alien_color == green_color:
    print("You earned 5 points.")
elif alien_color == yellow_color:
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

print("\nelif Version-------------------------------------")
alien_color = ('Yellow') 

green_color = ('Green')
yellow_color = ('Yellow')
red_color = ('Red')

if alien_color == green_color:
    print("You earned 5 points.")
elif alien_color == yellow_color:
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

print("\nelse Version-------------------------------------")
alien_color = ('Red') 

green_color = ('Green')
yellow_color = ('Yellow')
red_color = ('Red')

if alien_color == green_color:
    print("You earned 5 points.")
elif alien_color == yellow_color:
    print("You earned 10 points.")
else:
    print("You earned 15 points.")