#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "circuit.py", "14/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

calc = {}
results = {}

for command in open('inp.txt'):
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]
a = calculate('a')
print("a: {}".format(calculate('a')))
calc['b'] = [str(a)]
results = {}
print("new a: {}".format(calculate('a')))