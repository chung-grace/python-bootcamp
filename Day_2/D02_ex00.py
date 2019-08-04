#!/usr/bin/env python3
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program

# Please write a docstring for every function you write.

###############################################################################
# Imports
import random

# Body


###############################################################################
def main():
    
    # Create random integer from 1 - 25
    randNum = random.randint(1,25)
    
    #For loop to iterate five times -> only lets the user guess five times
    for i in range(0,5): 
        # Asks the user to guess what the number is
        try:
            x = int(input("Give me a number: "))
        #Validates input is a number
        except ValueError:
            print("You screwed something up...")
        # Tells the user if they guessed correctly, if yes exit the loop
        if x == randNum:
            print("You guessed correctly")
            break
        # If the guessed number is too high, then tell the user that it's too high
        elif x > randNum:
            print("Too high!")
            
        # If the guessed number is too low, then tell the user that it's too low
        elif x < randNum: 
            print("Too low!")

#execute the main function
if __name__ == '__main__':
    main()
