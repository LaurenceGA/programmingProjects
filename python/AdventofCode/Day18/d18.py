#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "d18.py", "18/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


data = [line.rstrip() for line in open('inp.txt')]

# data = ['.#.#.#',
#         '...##.',
#         '#....#',
#         '..#...',
#         '#.#..#',
#         '####..']

lights_grid = []

for line in data:
    row = []
    for char in line:
        row.append(1 if char == '#' else 0)
    lights_grid.append(row)

lights_grid[0][0] = 1
lights_grid[0][len(lights_grid)-1] = 1
lights_grid[len(lights_grid)-1][0] = 1
lights_grid[len(lights_grid)-1][len(lights_grid)-1] = 1


def neighbours(coord, max):
    neighb = []
    for j in range(-1, 2):
        for i in range(-1, 2):
            if coord[0] + i < 0 or coord[1] + j < 0 or coord[0] + i > max - 1 or coord[1] + j > max - 1 or \
                    (i == 0 and j == 0):
                continue
            neighb.append((coord[0] + i, coord[1] + j))
    return neighb


def step(grid):
    from copy import deepcopy
    ref_grid = deepcopy(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if (i == 0 and j == 0) or (i == len(grid)-1 and j == 0) or (j == len(grid)-1 and i == 0) or \
                    (i == len(grid)-1 and j == len(grid)-1):
                continue

            neighbs = neighbours((i, j), len(grid))
            if ref_grid[j][i] == 1:
                num_on = 0
                for n in neighbs:
                    if ref_grid[n[1]][n[0]] == 1:
                        num_on += 1

                if not (num_on == 2 or num_on == 3):
                    grid[j][i] = 0

            else:
                num_on = 0
                for n in neighbs:
                    if ref_grid[n[1]][n[0]] == 1:
                        num_on += 1

                if num_on == 3:
                    grid[j][i] = 1


for i in range(100):
    step(lights_grid)
    # for l in lights_grid:
    #     for c in l:
    #         if c == 1:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()
    # print()

on = 0
for i in lights_grid:
    on += sum(i)
print(on)
