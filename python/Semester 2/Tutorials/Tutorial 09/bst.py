#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "bst.py", "1/10/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import random


class BSTMap:
    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, key, value):
        node = self._bstSearch(self._root, key, key)
        node = None if len(node) == 0 else node[0]  # Grab the node if it exists

        if node is not None:
            node.value = value
            return False
        else:
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True

    def _bstInsert(self, subtree, key, value):
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bstInsert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bstInsert(subtree.right, key, value)
        return subtree

    # A method to visualise a tree
    def print_tree(self):
        self._root.print_node()

    def _bstSearch(self, subtree, minimum, maximum):
        nodes_in_range = []
        if subtree is None:
            return nodes_in_range
        elif subtree.key < minimum:     # Below range
            nodes_in_range.extend(self._bstSearch(subtree.right, minimum, maximum))
        elif subtree.key > maximum:     # Above range
            nodes_in_range.extend(self._bstSearch(subtree.left, minimum, maximum))
        else:   # In range
            nodes_in_range.append(subtree)
            nodes_in_range.extend(self._bstSearch(subtree.left, minimum, maximum))
            nodes_in_range.extend(self._bstSearch(subtree.right, minimum, maximum))
        return nodes_in_range

    def valueOf(self, minimum, maximum):    # Called minimum and maximum as not to shadow python's min & max functions
        nodes = self._bstSearch(self._root, minimum, maximum)
        values_dict = {}
        for node in nodes:
            assert node is not None, "Invalid map key."
            values_dict[node.key] = node.value
        return values_dict


class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    # Functions to help visualize what's going on
    def __str__(self):
        return "(${}, {})".format(self.key, self.value)

    def print_node(self, level=0):
        if self.right:
            self.right.print_node(level+1)
        print "{}>${}: {}".format("|\t" * level, self.key, self.value)
        if self.left:
            self.left.print_node(level+1)

# TESTING FROM HERE
if __name__ == "__main__":
    # Create a tree to test on
    prices = BSTMap()
    # Set some testing variables
    max_price = 50
    num_items = 20

    # Random things to have as cargo
    sale_items = ('toy', 'wallet', 'game', 'pair of shoes', 'glasses',
                  'T-shirt', 'book', 'pants', 'jacket', 'jumper', 'chair',
                  'belt', 'figurine', 'handbag', 'football')

    # Make the root roughly in the middle just to make things nicer
    prices.add(max_price // 2, random.choice(sale_items))
    # Generate a population of lists to pull from
    price_list = [round((random.random() * max_price)*100)/float(100) for k in range(num_items)]
    for i in range(num_items):
        prices.add(random.choice(price_list), random.choice(sale_items))

    # Visualise the tree
    prices.print_tree()

    values = prices.valueOf(10, 25)
    print "\nObjects prices between between $10 and $25 ({} of {} items)".format(len(values), num_items)
    # Print nicely
    for price, obj in values.items():
        print "{} for ${}".format(obj, price)
