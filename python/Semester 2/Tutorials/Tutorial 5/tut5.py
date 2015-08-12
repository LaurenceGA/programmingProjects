#!/usr/bin/env python
from sys import stdout
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "tut5.py", "10/08/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

# Read in data from a file and put it into a python list
file = open("example_sorted_names.txt")

names_list = []
for line in file:
    line = line.strip()
    names_list.append(line)

file.close()

# for line in names_list:r
#     print line


def binary_search(the_list, lower, upper, item):
    item = item.lower()
    if lower > upper:
        print "The item was not in the list"
        return -1

    middle_pos = (lower + upper) // 2
    
    if the_list[middle_pos][0].lower() < item:
        lower = middle_pos + 1
        return binary_search(the_list, lower, upper, item)
    elif the_list[middle_pos][0].lower() > item:
        upper = middle_pos - 1
        return binary_search(the_list, lower, upper, item)
    else:
        if middle_pos == 0:
            return 0
        else:
            i = 1
            while the_list[middle_pos - i][0].lower() == item.lower():
                if middle_pos - i <= 0:
                    return 0
                i += 1

            return middle_pos - i + 1


def names_beginning(the_list, char):
    names_start = binary_search(the_list, 0, len(the_list)-1, char)
    # print names_start
    i = names_start
    while the_list[i][0].lower() == char.lower():
        print the_list[i]
        i += 1

        if i >= len(the_list):
            break
    # for name in the_list:
    #     if name[0].lower() == char:
    #         print name

# names_beginning(names_list, 'H')


def insertion_sort(the_list):
    # Start as position 1
    for i in range(1, len(the_list)):
        # Get val of item to insert
        name = the_list[i]

        # Value to left
        j = i - 1

        # Move down list to find insertion position
        while j >= 0 and len(the_list[j]) > len(name):
            the_list = the_list[:j] + [the_list[j+1]] + the_list[j+1:]
            j -= - 1

        the_list = the_list[:j] + [name] + the_list[j+1:]

insertion_sort(names_list)

for name in names_list:
    print name
