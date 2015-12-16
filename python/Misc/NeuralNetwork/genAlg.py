#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "genAlg.py", "14/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

from sim import Simulation, Fish
import random

class GenAlg(object):
    """
    Test
        Select
        Crossover
        Mutate
        ...Repeat
    ...Repeat
    """
    def __init__(self, population, screen, clock):
        self.generation = 1
        self.screen = screen
        self.clock = clock
        self.crossover_rate = 0.7
        self.mutation_rate = 0.001

        self.sim = [None]

        self.population = []
        for i in range(population):
            # Create instance
            self.population.append(Fish([screen.get_width()*random.random(), screen.get_height()*random.random()],
                                        self.screen, self.clock, self.sim))

        self.startSim()

    def startSim(self):
        self.sim[0] = Simulation(self.population, self.screen, self.clock)

    def update(self):
        if self.sim:
            self.sim[0].step()

    def draw(self):
        if self.sim:
            self.sim[0].draw()
