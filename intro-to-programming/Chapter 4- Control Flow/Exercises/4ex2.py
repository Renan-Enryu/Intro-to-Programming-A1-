# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# •If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# •If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# •Write one version of this program that runs the if block and another that runs the else block.

print("\nif Version-------------------------------------")

alien_color = ('Green')
real_color = ('Green')

if alien_color == real_color:
    print("You shot the alien, You earned 5 points.")
else:
    print("You saved the alien, You earned 10 points.")

print("\nelse Version-------------------------------------")

alien_color = ('Red')
real_color = ('Green')

if alien_color == real_color:
    print("You shot the alien, You earned 5 points.")
else:
    print("You saved the alien, You earned 10 points.")
