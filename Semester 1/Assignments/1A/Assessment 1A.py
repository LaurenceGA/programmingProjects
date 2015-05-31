#!/usr/bin/env python

import math
import random


def calCircleArea(radius):
    # This function returns the area of a circle based on a given radius
    return math.pi * radius**2

circleRadius = random.randint(1, 20)        # Find a random radius for the circle
numOfGuess = 0                              # How many guesses the user makes
userGuess = 0                               # Current guess made by the user

while userGuess != circleRadius:        # If they have not yet guessed correctly...
    # Get the input from the user
    userInput = input("The area of the circle is %.2f. Guess the radius(1-20):\n>>>" % calCircleArea(circleRadius))

    if userInput.lower() in ['exit', 'quit', 'q', 'i give up!']:    # Allow the user to exit with special input
        print("Goodbye!")                       # Say goodbye
        break                                   # Break from the loop to terminate the program. Could also use quit()

    try:                                            # A try/except is used to validate the user input and handle errors
        userGuess = int(userInput)                  # Convert to integer
        if not(userGuess > 20 or userGuess < 1):    # Make sure the guess is not out of range before continuing
            if userGuess > circleRadius:            # Too high?
                print("You guessed too high!")
            elif userGuess < circleRadius:          # Too low?
                print("You guess too low!")
            # The third condition of equality is already covered by the while loop
            numOfGuess += 1                 # Increment the number of guesses
        else:
            print("The radius is between 1 and 20 (inclusive), that is out of range.")
    except ValueError:                      # A ValueError is throw if the input can't be made an integer
        print("That is not a valid input, try again.")

else:   # Else will only be called if the above expression of the while loop is satisfied, i.e the user guesses correct
    guessString = "guesses"     # Just fixes the grammar of the output, using the
    if numOfGuess < 2:          #  singular or plural in the correct context
        guessString = "guess"
    print("Correct!\nThe radius was %d\nIt took you %d %s!" % (circleRadius, numOfGuess, guessString))
