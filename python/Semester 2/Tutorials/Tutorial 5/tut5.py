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


def insertion_sort(the_list):
    # Start as position 1
    for i in range(1, len(the_list)):
        # Get val of item to insert
        name = the_list[i]

        # Value to left
        j = i - 1

        # Move down list to find insertion position
        while j >= 0 and len(the_list[j]) > len(name):
            j -= 1

        the_list.insert(j+1, the_list.pop(i))   # Grab the current item and put into position


def selection_sort(the_list):
    for i in range(len(the_list)):
        min_pos = i

        # Scan to right
        for j in range(i+1, len(the_list)):
            if len(the_list[j]) < len(the_list[min_pos]):
                min_pos = j

        # Swap values
        the_list[i], the_list[min_pos] = the_list[min_pos], the_list[i]


def partition(the_list, bottom, top):
    pivot = len(the_list[bottom])

    h = bottom
    for k in range(h+1, top+1):
        if len(the_list[k]) < pivot:
            h += 1
            the_list[h], the_list[k] = the_list[k], the_list[h]

    the_list[bottom], the_list[h] = the_list[h], the_list[bottom]
    return h


def quick_sort(the_list, bottom=None, top=None):
    bottom = 0 if bottom is None else bottom
    top = len(the_list)-1 if top is None else top

    if bottom < top:
        split = partition(the_list, bottom, top)

        quick_sort(the_list, bottom, split-1)
        quick_sort(the_list, split+1, top)
    else:
        return

def sort_by_length(names):
    from time import clock
    start = clock()
    # selection_sort(names)
    # insertion_sort(names)
    quick_sort(names)
    print clock() - start

# names_beginning(names_list, 'H')
sort_by_length(names_list)

# for name in names_list:
#     print name

