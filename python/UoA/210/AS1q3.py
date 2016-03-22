#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "AS1q3.py", "16/03/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


def bits_to_float(bits):
    print("bits:", end="")
    for i in range(4):
        print(" " + bits[i*8:i*8+8], end="")
    print()

    print("sign bit: ", end="")
    print('+' if bits[0] == '0' else '-')
    sgn = -1 if bits[0] == '1' else 1

    exp_bits = bits[1:9]
    print("exponent bits: {} = {}".format(exp_bits, int(exp_bits, 2) - 127))
    exp = int(exp_bits, 2) - 127

    frac_bits = bits[9:]
    frac = 1
    for i in range(len(frac_bits)):
        # print(int(frac_bits[i])*(2**(-i+1)))
        frac += int(frac_bits[i])*(2**(-i-1))
    as_num = sgn * frac * 2**(exp)

    print("fraction bits: {}".format(frac_bits))
    print("as an integer: {}".format(int(as_num)))
    print("as a float: {}".format(float(as_num)))


bits_to_float("01000010110010000000000000000000")
