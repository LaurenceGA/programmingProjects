#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "camel.py", "16/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print authorship_string,

import random

# Give the camel a name in order to form an emotional attachment
camel_name = random.choice(("Dave",
                            "Geoff",
                            "Jerry",
                            "Douglas",
                            "Sarah",
                            "Betty",
                            "Amy",
                            "Lucy",
                            "Johnny",
                            "Mary",
                            "Matthew",
                            "Mark",
                            "Luke",
                            "John",
                            "Anne",
                            "Lisa"
                            ))

# Introduction
print "Welcome to Camel!"
print "You have stolen a camel named {} to make you way across the great Mobi desert.".format(camel_name)
print "The natives want {} back and are chasing you down!".format(camel_name)
print "Survive your desert trek and outrun the natives\n"


def offer_choice():
    # Options for the player
    print "A. Drink from your canteen."
    print "B. Ahead moderate speed."
    print "C. Ahead full speed."
    print "D. Stop and let {} rest for the night.".format(camel_name)
    print "E. Status check."
    print "Q. Quit\n"
    user_choice = raw_input("Your choice? ")

    return user_choice.lower()      # Case insensitive


def show_status(miles, drinks, natives):
    print "\nYou and {} have traveled: {} miles".format(camel_name, miles)
    print "Drinks in canteen: {}".format(drinks)
    print "The natives are {} miles behind you, but seem to be getting closer\n".format(natives)

done = False

max_drinks = 3

miles_traveled = 0
thirst = 0
camel_tiredness = 0

canteen_drinks = max_drinks
natives_distance = -20

while not done:
    user_choice = offer_choice()

    # USER CHOICES #

    if user_choice == 'q':
        done = True
    elif user_choice == 'a':
        # Drink from canteen
        if canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
            natives_distance += random.randint(2, 4)

            print "\nYou drink from your canteen\n"
        else:
            print "\nYou can't! You don't have any drinks left!!\n"

    elif user_choice == 'b':
        # Ahead at moderate speed
        travel = random.randint(7, 10)
        miles_traveled += travel
        thirst += 1
        camel_tiredness += 1
        natives_distance += random.randint(7, 10)

        print "\nYou traveled {} miles!\n".format(travel)

    elif user_choice == 'c':
        # Ahead at full speed
        travel = random.randint(12, 17)
        miles_traveled += travel
        thirst += random.randint(1, 2)
        camel_tiredness += random.randint(2, 3)
        natives_distance += random.randint(7, 10)

        print "\nYou traveled {} miles!\n".format(travel)

    elif user_choice == 'd':
        # Take a rest
        camel_tiredness = 0
        natives_distance += random.randint(7, 10)

        print "\n{} is happy\n".format(camel_name)

    elif user_choice == 'e':
        # Show status
        show_status(miles_traveled, canteen_drinks, miles_traveled - natives_distance)
        natives_distance += random.randint(2, 4)    # Penalty for checking status
    else:
        print "That's not a valid command!\n"
        continue

    # RANDOM EVENTS #

    # Maybe find an Oasis
    if random.randint(1, 20) == 1:
        print "You found an Oasis!\n"
        canteen_drinks = max_drinks
        thirst = 0
        camel_tiredness = 0
    # Sandstorm
    elif random.randint(1, 20) == 1:    # Actually 1/20 * 19/20 chance
        print "You run into a sandstorm! It's thirsty work\n"
        thirst += random.randint(2, 3)
    # Find a traveler
    elif random.randint(1, 20) == 1:    # Actually 1/20 * 19/20 * 19/20 chance
        print "You stumble upon a traveler\n"
        confront = False
        while True:
            approach = raw_input("Do you approach the traveler? ")
            if approach.lower() in ("no", 'nah', 'hell no', 'n'):
                print "You hurry away quickly.\n"
                confront = False
                break
            elif approach in ["yes", "yep", "y", "yeah"]:
                print "You approach cautiously\n"
                confront = True
                break
            else:
                print "That's not a valid input, try again\n"

        if confront:
            if random.randint(1, 10) == 1:
                print "The traveler it kind hearted and lets you swap canteens." \
                      " {} is bigger and filled to the brim!\n".format(random.choice(("His", "Hers")))
                max_drinks = max(max_drinks, random.randint(4, 6))  # Make it bigger unless it's already bigger
                canteen_drinks = max_drinks
            elif random.randint(1, 20) == 1:
                print "You chat for a bit but once you say your farewells you notice your canteen is missing! " \
                      "You turn around but the traveler is nowhere to be seen\n"
                canteen_drinks = 0
                max_drinks = 0
            elif random.randint(1, 40) == 1:
                print "While you're back was turned the traveler stabs you!\nYou died"
                print "He also stabs {0}, {0} also dies.\n".format(camel_name)
                print "You had traveled {} miles," \
                      " {} drinks were left in your canteen" \
                      " and the natives were {} miles behind you".format(miles_traveled,
                                                                         canteen_drinks,
                                                                         miles_traveled - natives_distance)
                done = True
            elif random.randint(1, 30) == 1:
                natives_distance += random.randint(4, 20)
                print "The traveler leaps at you and you fall from your camel." \
                      " The last thing you remember is the rabid whites of their eyes"
                print "You wake up dazed with {} licking at your face," \
                      " you don't know how long you were gone".format(camel_name)
                print "Nothing appears to be stolen and the traveler is gone\n"
            else:
                print "{} a generous one who gives you some water\n".format(random.choice(("He's", "She's")))
                canteen_drinks += random.randint(1, 2)
                # If you now have excess water, drink it if you are thirsty
                thirst -= max(0, canteen_drinks - max_drinks)
                canteen_drinks = min(canteen_drinks, max_drinks)
    # Lost water
    elif random.randint(1, 20) == 1:    # Actually 1/20 * 19/20 * 19/20 * 19/20 chance
        print "You discover there was a leak in your canteen!",
        if canteen_drinks == 0:
            print "Well it was empty anyway. You patch it up. You don't know whether to laugh or cry.\n"
        else:
            print "You patch it up, but you can tell it feels lighter.\n"
            canteen_drinks = max(0, canteen_drinks - random.randint(1, 2))

    # STATUS EVENTS #

    # Thirst
    if not done and thirst > 6:
        print "You died of thirst!\n"
        print "You had traveled {} miles," \
              " {} drinks were left in your canteen" \
              " and the natives were {} miles behind you".format(miles_traveled,
                                                                 canteen_drinks,
                                                                 miles_traveled - natives_distance)
        done = True
    elif not done and thirst > 4:
        print "You are thirsty!\n"

    # Camel tiredness
    if not done and camel_tiredness > 8:
        print "{} is dead.\n".format(camel_name)
        print "You had traveled {} miles," \
              " {} drinks were left in your canteen" \
              " and the natives were {} miles behind you".format(miles_traveled,
                                                                 canteen_drinks,
                                                                 miles_traveled - natives_distance)
        done = True
    elif not done and camel_tiredness > 4:
        print "{} is getting tired\n".format(camel_name)

    # Natives distance
    if not done and miles_traveled - natives_distance <= 0:
        print "The natives have caught you!"
        print "You had traveled {} miles," \
              " {} drinks were left in your canteen" \
              " and the natives were {} miles behind you".format(miles_traveled,
                                                                 canteen_drinks,
                                                                 miles_traveled - natives_distance)
        done = True
    elif miles_traveled - natives_distance <= 15:
        print "The natives are getting close!\n"

    # End game
    if not done and miles_traveled >= 200:
        print "After {} miles you and {} ride to safety".format(miles_traveled, camel_name)
        print "The natives were {} miles behind you" \
              " and you had {} drinks left in your canteen".format(miles_traveled - natives_distance, canteen_drinks)
        print "You won the game!!!"
        done = True