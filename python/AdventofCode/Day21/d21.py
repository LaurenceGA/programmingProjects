#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "d21.py", "21/12/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import re

inp = {
    'Hit Points': 109,
    'Damage': 8,
    'Armor': 2
}


class Item(object):
    def __init__(self, typ, name, cst, dmg, arm):
        self.typ = typ
        self.name = name
        self.cost = cst
        self.damage = dmg
        self.armor = arm

    def __str__(self):
        return "{}: cost({}), dmg({}), armor({})".format(self.name, self.cost, self.damage, self.armor)

shop_data = [line.rstrip() for line in open('test_items')]

shop = {}

header = None
for line in shop_data:
    if header is None:
        h = line.split()[0].replace(':', '')
        shop[h] = []
        header = h
        continue

    if line == '':
        header = None
        continue

    # item_info = [l.strip() for l in line.split()]
    m = re.match(R'(\w+|\w+\s+\+\d)\s+(\d+)\s+(\d+)\s+(\d+)$', line)
    # m = re.match(R'(.+)(\w+).*$', line)
    shop[header].append(Item(header, m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))


class Fighter(object):
    def __init__(self, hp, dmg=0, arm=0):
        self.health = hp
        self.damage = dmg
        self.armor = arm

        self.weapon = None
        self.armor_item = None
        self.rings = []

    def add_item(self, item):
        if item.typ == 'Weapons':
            if self.weapon:
                print("Can't have multiple weapons!")
            self.weapon = item
        elif item.typ == 'Armor':
            if self.armor:
                print("Can't have multiple Armor!")
            self.armor = item
        elif item.typ == 'Rings':
            if len(self.rings) >= 2:
                print("No more rings")
            self.rings.append(item)

        self.damage = self.get_attack()
        self.armor = self.get_def()

    def get_attack(self):
        attck = self.damage
        if self.weapon:
            attck += self.weapon.damage
        for r in self.rings:
            attck += r.damage
        return attck

    def get_def(self):
        defnse = self.armor
        if self.armor:
            defnse += self.armor_item.armor
        for r in self.rings:
            defnse += r.armor
        return defnse

    def take_damage(self, attack):
        attack -= self.armor
        self.health -= max(1, attack)

    def __str__(self):
        return "HP: {}, DMG: {}, ARM: {}".format(self.health, self.damage, self.armor)


boss = Fighter(inp['Hit Points'], inp['Damage'], inp['Armor'])
player = Fighter(100)

item_sets = [[]]

for i in shop['Weapons']:
    item_set = [i]
    pass

    item_sets.append(item_set)

def fight(f1, f2):
    f1_turn = True
    while f1.health > 0 and f2.health > 0:
        if f1_turn:
            f2.take_damage(f1.damage)
        else:
            f1.take_damage(f2.damage)

        f1_turn = not f1_turn

    if f1.health > 0:
        return 0
    else:
        return 1
