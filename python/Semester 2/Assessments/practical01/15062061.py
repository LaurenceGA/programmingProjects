#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "15062061.py", "2/08/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

# Laurence Armstrong - 15062061
# Practical programming test 1

# Problem set 1

# For spacing and clarity
print "Problem set 1."
print "##### Q1 #####\n"


# Q1
def join_list(string_list):     # Variable name changed to avoid shadowing built-in 'list'
    joined_string = ""      # Variable declared beforehand
    for string in string_list:
        joined_string += string
    return joined_string    # Return statement unindented so it's not part of the for loop

strings = ['learn ', 'computer ', 'science ', 'at ', 'Massey']   # Variable name changed to avoid shadowing
print join_list(strings)

# For spacing
print "\n##### Q2 #####\n"


# Q 2
def get_user_choice():
    while True:
        command = raw_input("Command: ")
        # '=' changed to '==' comparison operator. Each letter changed to string
        # Also would be more pythonic to say: if command in ['f', 'm'...] etc
        if command == 'f' or command == 'm' or command == 's' or command == 'd' or command == 'q':
            return command

        print "Hey, that's not a command. Here are your options:"
        print "f - Full speed ahead"
        print "m - Moderate speed"
        print "s - Status"
        print "d - Drink"
        print "q - Quit"

user_command = get_user_choice()
print "You entered: ", user_command

# Problem set 2

# For spacing
print "\nProblem set 2"
print "##### Q1 #####\n"

# Q1
for column in range(10):
    for n in range(10):
        print n,            # print number on same line
    print                   # Reset cursor

# For spacing
print "\n##### Q2 #####\n"

# Q2
for column in range(10):
    # Spaces first
    for i in range(column):
        print " ",      # Actually prints two spaces because of how print works, but this is what is wanted

    # Then numbers
    for j in range(10-column):
        print j,        # Extra space here means numbers match with extra space from before
    print


# Problem set 3

# For spacing
print "\nProblem set 3"
print "##### Q1 #####\n"


# Q1
def cap_first(string):
    return string[0].upper() + string[1:]   # Slice, capitalize then concatenate back together


def capitalize_nested(list_nest):
    # list_nest is a list of lists of strings
    new_list = []

    for nest in list_nest:
        inner = []      # New lists are created instead of modifying as a new list must be returned
        for word in nest:
            inner.append(cap_first(word))

        new_list.append(inner)

    return new_list

print capitalize_nested([['me', 'my'], ['you', 'youRs'], ['Them', 'their', 'theiRs']])

# For spacing
print "\n##### Q2 #####\n"


# Q2
def squares_list():
    # range(0, 100) gives 0-99, though 99 is odd so it doesn't change anything
    return [number**2 for number in range(0, 100) if number % 2 == 0]

print squares_list()


# Problem 4

# For spacing
print "\nProblem set 4\n"


def hailstone(n):
    print n,    # Print the number

    if n == 1:  # Terminate recursion case
        print   # Reset print cursor
        return

    # Next term in the sequence
    if n % 2 == 0:  # n is even
        hailstone(n / 2)
    else:   # n is odd
        hailstone(3*n+1)

hailstone(7)
