#!/usr/bin/env python
from sys import stdout
__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "Network.py", "6/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from NeuralNetwork.NLayer import NLayer


class NeuralNetwork(object):
    def __init__(self, num_input, num_output, num_hlayers, num_per_hidden):
        self.__input_layer = NLayer(num_input, False)   # Shouldn't transform values
        self.__hidden_layers = [NLayer(num_per_hidden) for i in range(num_hlayers)]
        self.__output_layer = NLayer(num_output, False)   # Shouldn't transform values

        self.__input_layer.connect(self.__hidden_layers[0])
        for l in range(1, len(self.__hidden_layers)-1):
            self.__hidden_layers[l].connect(self.__hidden_layers[l+1])
        self.__hidden_layers[-1].connect(self.__output_layer)

    def randomise(self, ammount):
        self.__input_layer.randomise(ammount)
        for l in self.__hidden_layers:
            l.randomise(ammount)
        self.__output_layer.randomise(ammount)

    def process(self, *inputs):
        if len(inputs) != len(self.__input_layer):
            raise ValueError("Incorrect number of inputs")

        self.__input_layer.get_values(*inputs)
        self.__input_layer.propegate()
        for l in self.__hidden_layers:
            l.evaluate()
            l.propegate()
        self.__output_layer.evaluate()

        return self.__output_layer.read_values()

    def __str__(self):
        s = ("I" * len(self.__input_layer)) + '\n'
        for l in self.__hidden_layers:
            s += ("X" * len(l)) + '\n'
        s += ("O" * len(self.__output_layer)) + '\n'
        return s
