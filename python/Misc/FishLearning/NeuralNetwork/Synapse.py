#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "Synapse.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import random


class Synapse(object):
    def __init__(self, nfrom, nto, strength):
        self.nfrom = nfrom
        self.nto = nto
        self.strength = strength

    def propegate(self, value):
        self.nto.recieve(value*self.strength)

    def randomise(self, ammount):
        self.strength += 2*(random.random()-0.5) * ammount
        self.strength = max(self.strength, 0)
        self.strength = min(self.strength, 1)
