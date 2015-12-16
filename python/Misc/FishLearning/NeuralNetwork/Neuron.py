#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "Neuron.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from math import exp


def sigmoid(x, deriv=False):
        if deriv:
            return x*(1-x)
        else:
            return 1/(1+exp(x))


def trivial_func(x):
    return x


class Neuron(object):
    def __init__(self, activ_func=True):
        self.value = 0
        self.synapses = []

        if activ_func:
            self.activation_func = sigmoid
        else:
            self.activation_func = trivial_func

        self.__inputs = []

    def recieve(self, value):
        self.__inputs.append(value)

    def send(self):
        for s in self.synapses:
            s.propegate(self.value)

    def evaluate(self):
        # Sum inputs, clear them and apply activation
        total = sum(self.__inputs)
        self.__inputs.clear()
        self.value = self.activation_func(total)

    def randomise(self, ammount):
        for s in self.synapses:
            s.randomise(ammount)
