#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("ExerciseA.py", "20/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def coin_toss():
    import random
    rand = random.randint(0, 1)
    if rand:
        return 'heads'
    else:
        return 'tails'

try:
    tails = 0
    heads = 0
    iterations = int(input("Number of times to toss the coin:"))

    for i in range(iterations):
        outcome = coin_toss()
        print(outcome)
        if outcome == 'heads':
            heads += 1
        else:
            tails += 1

    print("%d x heads; %d x tails" % (heads, tails))
    print("That's %.2f%% heads and %.2f%% tails" % (heads/(heads + tails)*100, tails/(heads + tails)*100))
except ValueError:
    print("Nope")