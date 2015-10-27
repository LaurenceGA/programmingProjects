#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "tut10.py", "7/10/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import random


# Generate a random prime number less than limit
def random_prime(limit):

    # The Sieve of Eratosthenes
    # -------------------------
    # First, create a table of natural numbers.  We "cross off" the numbers
    # that are not prime, leaving only the prime numbers.
    # This table is implemented as a dictionary where the keys are natural
    # numbers, and the values are set to False when we cross numbers off
    naturals = dict({(x, True) for x in range(0, limit)})
    naturals[0] = False     # 0 is not prime
    naturals[1] = False     # 1 is not prime

    # Make a table to hold all the confirmed prime numbers so we can
    # select one at random later
    primes = []
    n_primes = 0

    # Now iterate over the natural numbers.  For each one that isn't crossed
    # off yet, add it to the list of primes numbers, then cross off all
    # it's multiples.
    for i in range(2, limit):
        if naturals[i]:     # i is prime
            # so add i to our list of confirmed primes
            primes.append(i)
            n_primes += 1

            # and cross off the multiples of i (by setting them to False)
            for j in range(i * i, limit, i):
                naturals[j] = False

    return primes[random.randrange(n_primes)]


def mc_rabin_karp_search(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)

    assert pattern_length > 0 and text_length > 1, "Invalid parameters"     # Text length must be > 1 for primes to work
    assert text_length >= pattern_length, "Patterns can't be smaller than text length"

    q = random_prime(pattern_length*text_length**2)
    r = (2**(pattern_length-1)) % q
    # Computation of initial remainders
    fingerprint = [0]
    pfinger = 0

    for j in range(pattern_length):
        fingerprint[0] = (2*fingerprint[0] + ord(text[j])) % q
        pfinger = (2*pfinger + ord(pattern[j])) % q

    i = 0
    while i + pattern_length <= text_length:
        if fingerprint[i] == pfinger:
            print "match at position", i
            if text[i:i+pattern_length] != pattern:
                print "FALSE POSITIVE"

        if i+pattern_length != text_length:
            fingerprint += [(2*(fingerprint[i] - r*ord(text[i])) + ord(text[i+pattern_length])) % q]
        i += 1

print "hell in hello there"
mc_rabin_karp_search("hell", "hello there")

print "\n010101 in 001011010100101011"
mc_rabin_karp_search("010101", "001011010100101011")    # Prone to giving false positives

print "\nhi in hello heli heio hi hi hi"
mc_rabin_karp_search("hi", "hello heli heio hi hi hi")

print "\n01011 in 0010110101001010011"
mc_rabin_karp_search("01011", "0010110101001010011")    # Prone to giving false positives

print "\nTweedledum in Tweedledee and Tweedledum"
mc_rabin_karp_search("Tweedledum", "Tweedledee and Tweedledum")

print "\npappar in pappappapparrassanuaragh"
mc_rabin_karp_search("pappar", "pappappapparrassanuaragh")  # Prone to giving false positives

print "\ndrum in conundrum"
mc_rabin_karp_search("drum", "conundrum")

print "\npepper in peter piper picked a peck of pickled peppers. How many pickled peppers did peter piper pick?"
mc_rabin_karp_search("pepper", "peter piper picked a peck of pickled peppers. How many pickled peppers did peter piper pick?")
