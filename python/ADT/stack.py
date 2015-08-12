#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" %\
                    ("stack.py", "8/04/15", __author__, 15062061, "-----" * 15)\
                    if __name__ == '__main__' else ""
print(authorship_string, end="")


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []
