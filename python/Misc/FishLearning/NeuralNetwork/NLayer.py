#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "NLayer.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from NeuralNetwork.Neuron import Neuron
from NeuralNetwork.Synapse import Synapse

from random import random


class NLayer(object):
    def __init__(self, num_neurons, act_func=True):
        self.neurons = []
        for n in range(num_neurons):
            self.neurons.append(Neuron(activ_func=act_func))

    def get_values(self, *vals):
        for i in range(len(vals)):
            self.neurons[i].value = vals[i]

    def propegate(self):
        for n in self.neurons:
            n.send()

    def read_values(self):
        vals = []
        for n in self.neurons:
            vals.append(n.value)
        return vals

    def evaluate(self):
        for n in self.neurons:
            n.evaluate()

    def connect(self, other_layer):
        for i in range(len(self.neurons)):
            for j in range(len(other_layer.neurons)):
                self.neurons[i].synapses.append(Synapse(self.neurons[i], other_layer.neurons[j], random()))

    def randomise(self, amount):
        for n in self.neurons:
            n.randomise(amount)

    def __len__(self):
        return len(self.neurons)
