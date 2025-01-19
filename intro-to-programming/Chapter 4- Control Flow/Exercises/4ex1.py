# Imagine an alien was just shot down in a game. 
# Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •Write an if statement to test whether the alien’s color is green. 
# If it is, print a message that the player just earned 5 points.
# •Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

# alien_color = ('Green')
# real_color = ('Green')

# if alien_color == real_color:
#     print("That is the Correct Color, 5 points Added")
# else:
#     print("That is not the Aliens Color, No points added.")

# Version 1

alien_color = ('Green')
real_color = ('Green')

if alien_color == real_color:
    print("That is the Correct Color, 5 points Added")

# Version 2

alien_color = ('Yellow')
real_color = ('Green')

if alien_color == real_color:
    exit()