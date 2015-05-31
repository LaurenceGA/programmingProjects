#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("Money Dispenser.py", "20/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

amounts = [100, 50, 20, 5, 2, 1]

initial_amount = 0


def num_of(bal, amount):
    if bal // amount > 0:
        print("%d x $%d" % (bal // amount, amount))

try:
    initial_amount = int(input("Initial amount ($1-1000): "))

    if initial_amount > 1000:
        print("Too high")
        quit()
    elif initial_amount <= 0:
        print("You get nothing")
        quit()

except ValueError:
    print("That's not acceptable")

balance = initial_amount

for i in amounts:
    num_of(balance, i)
    balance %= i