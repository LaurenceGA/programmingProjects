#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Differential calculator.py", "7/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def get_parts(eqn):
    a = None
    var = None
    power = None
    for i, char in enumerate(eqn):
        if not a:
            if char.isalpha():
                a = eqn[:i]
                var = eqn[i:i+1]
                power = eqn[i+2:]

    return a, var, power


def derive_parts(a, var, power):
    if a:
        a = float(a)
    else:
        if var:
            a = 1
        else:
            a = 0
    if power:
        power = float(power)
    else:
        power = 1

    a *= power
    power -= 1

    return a, var, power


def form_derivative(a, var, power):
    if var:
        if power == 1:
            power = ""
        elif power == 0:
            power = ""
            var = ""
        else:
            power = "^{0:g}".format(power)

        if a == 0:
            a = '0'
            var = ""
            power = ""
        elif a == 1:
            if var:
                a = ""
            else:
                a = '1'
        elif a == -1:
            a = "-"
        else:
            a = "{0:g}".format(a)
    else:
        var = ""
        power = ""

    derivative = "{}{}{}".format(a, var, power)

    return derivative


def get_derivative(eqn):
    a, var, power = get_parts(eqn)
    a, var, power = derive_parts(a, var, power)

    return form_derivative(a, var, power)


def derive(eqn):
    eqn_parts = []
    part_start = 0
    part_end = 1

    for char in eqn:
        if (char in ['+', '-'] or part_end == len(eqn)) and not part_end == 1:
            if part_end == len(eqn):
                eqn_parts.append([eqn[part_start:part_end].strip(), ""])
            else:
                eqn_parts.append([eqn[part_start:part_end-1].strip(), char])
            part_start = part_end
        part_end += 1

    for i in range(len(eqn_parts)):
        eqn_parts[i][0] = get_derivative(eqn_parts[i][0])
        if eqn_parts[i][0] == '0':
            eqn_parts[i] = ('', '')
            if eqn_parts[i-1]:
                eqn_parts[i-1][1] = ''

        eqn_parts[i] = " ".join(eqn_parts[i])

    final_eqn = " ".join(eqn_parts)

    return final_eqn

equation = input("Enter an equation: ")


print("The derivative is {}".format(derive(equation)))
