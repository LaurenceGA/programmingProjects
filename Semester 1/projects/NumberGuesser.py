__author__ = 'laurence'

import random

numsToGuess = 1000
maxNum = 100000
totalGuesses = 0


def guessnumber():
    guesses = 0
    randi = random.randint(0, maxNum)
    print("Guessing numbers betweeen 0 and %d" % maxNum)
    lowest = 0
    highest = maxNum
    guess = 0

    while not guess == randi:
        if (highest - lowest) == 1:
            guess = int(lowest + (highest - lowest)/2) + 1
        else:
            guess = int(lowest + (highest - lowest)/2)
        print("Guessing %d" % guess)
        if guess > randi:
            highest = guess
            print("Lower")
        elif guess < randi:
            lowest = guess
            print("Higher!")
        else:
            print("Correct! The number was %d" % randi)

        guesses += 1

    return guesses

for i in range(numsToGuess):
    g = guessnumber()
    totalGuesses += g
    print("Took %d gusses" % g)
else:
    print("\n\nAttempted to find a number between 0 and %d, %d times. %d guesses required on average. %d guesses made in total." % (maxNum, numsToGuess, totalGuesses/numsToGuess, totalGuesses))