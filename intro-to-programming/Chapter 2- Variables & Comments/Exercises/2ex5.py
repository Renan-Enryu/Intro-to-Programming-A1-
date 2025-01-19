# A girl heads to a computer shop to buy some USB sticks. 
# She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
# You will to use the arithmetic operators to complete this exercise.

usbc = 6
money = 50

usbamount = money // usbc
moneyleft = money % usbc

print("She can afford to get:",usbamount,"usbs","\nAnd she will have:",moneyleft,"left")