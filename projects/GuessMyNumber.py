__author__ = 'laurence'

import random

maxNum = 1000
randNum = random.randint(1, maxNum)

guessesMade = 0

rawInp = input("Guess a number between 1 and %d\n>>>" % maxNum)


def checkinp(inp):
    global guessesMade
    if not inp.isdigit():
        print("That's not valid")
        return -1

    if '.' in inp:
        print("That isn't an integer!")
        return -1

    num = int(inp)

    if num > 0 and num <= maxNum :
        guessesMade += 1
        return num
    else:
        print("That's not within the given range!")
        return -1

guess = checkinp(rawInp)


def getinp():
    global guess
    while guess < 0:
        guess = checkinp(input("Guess again\n>>>"))
    else:
        if guess > randNum:
            print("Lower!")
            guess = checkinp(input("Guess again\n>>>"))
            getinp()
        elif guess < randNum:
            print("Higher!")
            guess = checkinp(input("Guess again\n>>>"))
            getinp()
        elif guess == randNum:
            print("Correct!")
            print("It only took you %d guesses" % guessesMade)

getinp()