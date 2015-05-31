myName = "laurence"

userGuess = ""

while userGuess != myName:
    userGuess = input("What is my name? ").lower()

    if userGuess == myName:
        print("Got it!")
    else:
        print("Guess again")