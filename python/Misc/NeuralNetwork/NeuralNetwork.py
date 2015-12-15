#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "NeuralNetwork.py", "7/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))


class NeuralLayer(object):
    weight_scale = 6

    def __init__(self, nneurons, code_bits):
        self.code_bits = code_bits
        self.values = np.zeros(nneurons, dtype=float)
        self.length = nneurons
        self.weights = None

    def connect(self, next_len=None, code_bytes=None):
        if code_bytes:
            weight_ints = []
            for i in code_bytes:
                sign = -1 if i[0] == '1' else 1
                weight_ints.append(sign*int(i[1:], 2))
            weight_ints = np.array(weight_ints)
            scale = (2**(self.code_bits-1))
            self.weights = weight_ints / scale * self.weight_scale
            self.weights = self.weights.reshape((len(self), len(code_bytes)/len(self)))
        else:
            # self.weights = (np.random.randn(len(self.values), next_len) - 0.5)*2
            scale = (2**(self.code_bits-1))
            self.weights = np.random.randint(-(scale/2),
                                             scale/2 - 1,
                                             (len(self.values), next_len)) / scale * self.weight_scale
            code = ''
            for r in self.weights:
                for c in r:
                    val = int((c/self.weight_scale)*scale)
                    code += '1' if val < 0 else '0'
                    code += format(abs(val), '0' + str(self.code_bits-1) + 'b')
            # print(self.weights)
            return code

    def set_vals(self, vals):
        self.values = np.array(vals, dtype=float)

    def forward(self, next_layer):
        vals = np.dot(self.values, self.weights)
        vals = sigmoid(vals)
        next_layer.values = vals

    def __len__(self):
        return self.length


class NeuralNetwork(object):
    """
    On creation requires:
    ninputs     Number of input neurons
    noutputs    Number of output neurons
    nhlayers    Number of hidden layers
    nperhlayer  Number of neurons per hidden layer

    nperhlayer can be a single value or a list for the number for each layer
    """
    gcode_bits = 8

    def __init__(self, ninputs, noutputs, nhlayers, nperhlayer, gcode=''):
        self.gcode = ''

        self.inputs = NeuralLayer(ninputs, self.gcode_bits)
        self.hlayers = []

        if gcode:
            if len(gcode) % 8 != 0:
                raise ValueError("Incorrect code length")
            else:
                self.gcode = gcode

        try:
            if not len(nperhlayer) == nhlayers:
                raise ValueError("nperhlayer not of correct length")
        except TypeError:
            nperhlayer = [nperhlayer] * nhlayers

        for i in range(nhlayers):
            self.hlayers.append(NeuralLayer(nperhlayer[i], self.gcode_bits))

        self.outputs = NeuralLayer(noutputs, self.gcode_bits)

        # Connect it up
        if self.gcode:
            # Chop up genetic code
            code_bytes = [self.gcode[i:i+self.gcode_bits] for i in range(0, len(self.gcode), self.gcode_bits)]
            place = 0

            n_connections = len(self.hlayers[0])*len(self.inputs)
            self.inputs.connect(code_bytes=code_bytes[place:place+n_connections])
            place += n_connections

            for i in range(len(self.hlayers)-1):
                n_connections = len(self.hlayers[i])*len(self.hlayers[i+1])
                self.hlayers[i].connect(code_bytes=code_bytes[place:place+n_connections])
                place += n_connections

            n_connections = len(self.hlayers[0])*len(self.outputs)
            self.hlayers[-1].connect(code_bytes=code_bytes[place:place+n_connections])

            # print(code_bytes)
        else:
            # Inputs
            self.gcode += self.inputs.connect(len(self.hlayers[0]))

            # Hidden layers
            for i in range(len(self.hlayers)-1):
                self.gcode += self.hlayers[i].connect(len(self.hlayers[i+1]))

            # Outputs
            self.gcode += self.hlayers[-1].connect(len(self.outputs))

    def process(self, *inputs):
        # Load inputs
        if len(inputs) == len(self.inputs):
            self.inputs.set_vals(inputs)
        else:
            raise ValueError("Incorrect number of inputs")

        self.inputs.forward(self.hlayers[0])

        for i in range(len(self.hlayers)-1):
            self.hlayers[i].forward(self.hlayers[i+1])

        self.hlayers[-1].forward(self.outputs)

        return self.outputs.values


