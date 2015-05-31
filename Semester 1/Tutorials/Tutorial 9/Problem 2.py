#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem 2.py", "18/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

balance = 0

ledger = []


def set_balance(amount):
    global balance

    balance = amount


def print_balance():
    global balance
    print("Current balance is ${}".format(balance))


def print_ledger_line(date, amount, details):
    global balance, ledger
    print("{:12}{:45}${:<8}${:<8}".format(date, details, amount, balance))


def deposit(date, details, amount):
    global balance, ledger

    balance += amount
    print_ledger_line(date, amount, details)


def withdraw(date, details, amount):
    global balance, ledger
    if amount <= balance:
        balance -= amount
        print_ledger_line(date, -amount, details)
    else:
        print("You don't have that much money!")

set_balance(500)
print_balance()
withdraw("17-12-2012", "BP - petrol", 72.50)
withdraw("19-12-2012", "Countdown", 55.50)
withdraw("20-12-2012", "munchies", 1.99)
withdraw("22-12-2012", "Vodafone", 20)
deposit("23-12-2012",  "Income", 225)
withdraw("24-12-2012", "Presents", 99.02)
print_balance()