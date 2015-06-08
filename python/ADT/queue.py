#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("queue.py", "9/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        from ADT.node import Node
        node = Node(cargo)
        if self.head is None:
            # If list is empty, new node goes first
            self.head = self.last = node
        else:
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None

        return cargo


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items()

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item