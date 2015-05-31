#!/usr/bin/env python
# 159.171 Assignment 1B
# Laurence Armstrong, 15062061
__author__ = 'Laurence Armstrong'
authorship_string = "%s created by %s (%d)\n%s\n" % \
                    ("AdCreator.py", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

import random

description = ['First', 'Dream', 'New Family', 'Brand New']
adjective = ['Wonderful', 'Sunny', 'Spacious', 'Secluded']
bedrooms = [1, 2, 3, 4, 5]
suburb = ['Hokowhitu', 'Fitzherbert', 'Cloverlea', 'Terrace End', 'Kelvin Grove']
type_of_owner = ['a couple', 'a family', 'a retired couple', 'a large family', 'a professional couple']
amenities_close_by = ['great schools', 'a shopping centre', 'the motorway', 'the airport', 'a hospital']

advertisement = """*** Your %s Home ***
%s %d bedroom home in %s
Would suit %s
Close to %s
All enquiries to Joe Bloggs on 007 1234
*** Make it yours today! ***
""" % (random.choice(description),
random.choice(adjective),
random.choice(bedrooms),
random.choice(suburb),
random.choice(type_of_owner),
random.choice(amenities_close_by))

print(advertisement)