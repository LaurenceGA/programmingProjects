#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("PaperScissorRock.py", "20/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

player_wins = 0
computer_wins = 0

def get_input():
    """
    0 = paper
    1 = scissors
    2 = rock
    """
    inp = input("Paper, scissors or rock? ")
    if inp.lower() in ['p', 'paper', '0']:
        return 0
    elif inp.lower() in ['s', 'scissors', '1']:
        return 1
    elif inp.lower() in ['r', 'rock', '2']:
        return 2
    else:
        raise ValueError


def conv_str(num):
    if num == 0:
        return 'paper'
    elif num == 1:
        return 'scissors'
    elif num == 2:
        return 'rock'


def play():
    global player_wins, computer_wins
    import random

    print("-" * 30)
    try:
        player = get_input()
    except ValueError:
        print("Try again")
        player = get_input()

    computer = random.randint(0, 2)
    print("Computer says %s!\n" % conv_str(computer))

    if player == computer:
        print("It's a tie! Go again.")
        play()
    elif (player-1) % 3 == computer:
        print("Player wins!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

    show_stats()
    print("-" * 30)

    if input("Play again?").lower() in ['y', 'yes', 'yep', 'aight', 'yeah']:
        play()
    else:
        quit()


def show_stats():
    global player_wins, computer_wins
    print("\nThe player has won %d times, the computer has won %d times" % (player_wins, computer_wins))

print()
play()