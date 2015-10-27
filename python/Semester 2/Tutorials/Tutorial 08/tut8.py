#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "tut8.py", "28/09/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import random


def linear_probe(home, index):
    return home + index


def quadratic_probe(home, index):
    return home + index**2


def insert(table, key, probe):
    number_of_collisions = 0
    hash_pos = key % len(table)
    probe_pos = 0
    # Keep probing until it's fine
    while table[(probe(hash_pos, probe_pos)) % len(table)] is not None:
        probe_pos += 1
        number_of_collisions += 1

    table[probe(hash_pos, probe_pos) % len(table)] = key    # Insert the key

    return number_of_collisions


def test_table(length, item_num, probe):
    h_table = [None] * length
    total_collisions = 0
    collisions_list = []
    items_list = random.sample(range(10000), item_num)
    for k, item in enumerate(items_list):
        total_collisions += insert(h_table, item, probe)
        if k % 10 == 0:     # Every 10 collisions (including 0 at start)
            collisions_list.append(total_collisions)

    return collisions_list


def comp_lists(list1, list2):
    def comp_elem(elem1, elem2):
        return 1 if elem1 < elem2 else 2
    return map(comp_elem, list1, list2)

# Most of the time quadratic probe is the best, linear probe is better with a lower load factor
lin_collisions = test_table(1009, 1000, linear_probe)
quad_collisions = test_table(1009, 1000, quadratic_probe)
print lin_collisions      # Uncomment to see actual values
print quad_collisions      # Uncomment to see actual values
print "for table size 1009, 1000 entries: \n", comp_lists(lin_collisions, quad_collisions)

# Double size
# Usually quadratic probe is best here, regardless of load
lin_collisions = test_table(2081, 2000, linear_probe)       # 20081 is prime
quad_collisions = test_table(20081, 2000, quadratic_probe)
# print lin_collisions      # Uncomment to see actual values
# print quad_collisions      # Uncomment to see actual values
print "for table size 20081, 2000 entries: \n", comp_lists(lin_collisions, quad_collisions)

# Half size
# Sometimes linear probe is okay here, linear probe is usually better at lower load factors
lin_collisions = test_table(509, 500, linear_probe)       # 509 is prime
quad_collisions = test_table(509, 500, quadratic_probe)
# print lin_collisions      # Uncomment to see actual values
# print quad_collisions      # Uncomment to see actual values
print "for table size 509, 500 entries: \n", comp_lists(lin_collisions, quad_collisions)
