#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "p1.py", "4/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def get_number(prompt, whichType):
    if whichType not in [float, int]:
        return None

    while True:
        try:
            number = whichType(input(prompt))
            return number
        except ValueError as e:
            print("Invalid input!", e)

height = get_number("How tall are you? ", float)
howMany = get_number("How many do you want? ", int)

print("You get {} {}cm tall monkeys".format(howMany, height))