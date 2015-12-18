#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "HungryScience.py", "15/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re, itertools

inp = ["Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2",
       "Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9",
       "Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1",
       "Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"]

ingr_tsp = 100


class Ingredient(object):
    def __init__(self, name, cap, dur, flav, text, cal):
        self.name = name
        self.cap = cap
        self.dur = dur
        self.flav = flav
        self.text = text
        self.cal = cal

    def __str__(self):
        return "{}: capacity {}, durability {}, flavor {}, texture {}, calories {}".format(self.name,
                                                                                           self.cap,
                                                                                           self.dur,
                                                                                           self.flav,
                                                                                           self.text,
                                                                                           self.cal)


class Recipe(object):
    def __init__(self, portions, ingredients):
        if len(portions) != len(ingredients):
            raise ValueError("Wrong lengths")

        self.portions = portions

        self.cap = max(sum([por*ingredients[i].cap for i, por in enumerate(portions)]), 0)
        self.dur = max(sum([por*ingredients[i].dur for i, por in enumerate(portions)]), 0)
        self.flav = max(sum([por*ingredients[i].flav for i, por in enumerate(portions)]), 0)
        self.text = max(sum([por*ingredients[i].text for i, por in enumerate(portions)]), 0)
        self.cal = max(sum([por*ingredients[i].cal for i, por in enumerate(portions)]), 0)

        self.score = self.cap*self.dur*self.flav*self.text

    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return str(self.score) + ' ' + str(self.portions)


cookie_ingredients = []

for i in inp:
    m = re.match(R"(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", i)
    cookie_ingredients.append(Ingredient(m.group(1),
                                         int(m.group(2)),
                                         int(m.group(3)),
                                         int(m.group(4)),
                                         int(m.group(5)),
                                         int(m.group(6))))

recipes = []
possible_indexes = itertools.combinations(range(ingr_tsp+len(cookie_ingredients)-1), len(cookie_ingredients)-1)

for inds in possible_indexes:
    recipe = [inds[0]]
    left = ingr_tsp - inds[0]
    for i, ind in enumerate(inds[1:]):
        portion = ind - inds[i] - 1
        recipe.append(portion)
        left -= portion
    recipe.append(left)

    recipes.append(Recipe(recipe, cookie_ingredients))

low_carb = [r for r in recipes if r.cal == 500]
print(low_carb)
print(max(low_carb))
