
"""

Program Name: Lab 5 - Dice Rolling Terms

Name: Elijah Drakeford

Purpose: Based on the dice that was rolled, the program will print the appropiate term for the roll.

Date: Feb 10, 2026

"""

# this is created for pr request
import random

message = ''
while message != 'done':
    message = input("\nRoll the dice? (Enter 'done' to exit the program): ")
    
    # generating dice values and total value
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    total_value = dice_one + dice_two

    # printing dice and total roll
    print("Dice Values:",dice_one, "," ,dice_two,)
    print("Total Roll: ",total_value)

    # if statement to determine the term for the roll
    if total_value == 2:
        print("Snake Eyes")
    elif total_value == 3:
        print("Ace Caught a Deuce")
    elif total_value == 5:
        print("Little Phoebe")
    elif total_value == 9:
        print("Nina from Pasadena")
    elif total_value == 11:
        print("Six Fice no Jive")
    elif total_value == 12:
        print("Boxcars")
    elif dice_one == 2 and dice_two == 2:
        print("Little Joe From Kokomo")
    elif dice_one == 3 and dice_two == 3:
        print ("Jimmy Hicks from the Sticks")
    elif dice_one == 4 and dice_two == 4:
        print("Eighter from Decatur")
    elif dice_one == 5 and dice_two == 5:
        print("Puppy Paws")
    elif (dice_one == 6 and dice_two == 1) or (dice_one == 1 and dice_two == 6):
        print("Six Ace")
    
    
