#!/usr/bin/env python
# 159.171 Assignment 1B
# Laurence Armstrong, 15062061
__author__ = 'Laurence Armstrong'
authorship_string = "%s created by %s (%d)\n%s\n" % \
                    ("InvestmentCalc.py", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

def calcInvestment(P, j, t):
    return P*(1 + (j / 12))**(12*t)

try:
    initVal = float(input("Initial investment amount: "))
    interest = float(input("Annual interest rate (%): "))/100
    years = float(input("Years amount will be invested for: "))

    # print("In %.f years time the value of the investment will be $%.2f" % (years, calcInvestment(initVal, interest, years)))
    print("In {:.0f} years time the value of the investment will be ${:.2f}".format(years, calcInvestment(initVal, interest, years)))
except ValueError:
    print("That's not an acceptable input.")