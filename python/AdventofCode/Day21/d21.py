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

shop_data = [line.rstrip() for line in open('shop_items.txt')]

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

    m = re.match(R'(\w+|\w+\s+\+\d)\s+(\d+)\s+(\d+)\s+(\d+)$', line)
    # print(m.groups())
    shop[header].append(Item(header, m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))

shop['Armor'].append(Item('Armor', 'None', 0, 0, 0))


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
            if self.armor_item:
                print("Can't have multiple Armor!")
            self.armor_item = item
        elif item.typ == 'Rings':
            if len(self.rings) >= 2:
                print("No more rings")
            self.rings.append(item)

        self.damage = self.get_attack()
        self.armor = self.get_def()

    def get_attack(self):
        attck = 0
        if self.weapon:
            attck += self.weapon.damage
        for r in self.rings:
            attck += r.damage
        return attck

    def get_def(self):
        defnse = 0
        if self.armor_item:
            defnse += self.armor_item.armor
        for r in self.rings:
            defnse += r.armor
        return defnse

    def take_damage(self, attack):
        attack -= self.armor
        self.health -= max(1, attack)

    def __str__(self):
        return "HP: {}, DMG: {}, ARM: {}".format(self.health, self.damage, self.armor)


item_sets = []

for i in shop['Weapons']:
    item_set = [i]
    item_sets.append(item_set)
    for j in shop['Armor']:
        new_item_set = item_set[:]
        new_item_set.append(j)
        item_sets.append(new_item_set)
        for lring in shop['Rings']:
            new_ring_item_set = new_item_set[:]
            new_ring_item_set.append(lring)
            item_sets.append(new_ring_item_set)
            for rring in shop['Rings']:
                if rring != lring:
                    new_rring_item_set = new_ring_item_set[:]
                    new_rring_item_set.append(rring)
                    item_sets.append(new_rring_item_set)


def fight(f1, f2):
    f1_turn = True
    # print(f1)
    # print(f2)
    # print('Boss hp {}, player hp {}'.format(f2.health, f1.health))
    while f1.health > 0 and f2.health > 0:

        if f1_turn:
            f2.take_damage(f1.damage)
            # print('boss on {}'.format(f2.health))
        else:
            f1.take_damage(f2.damage)
            # print('player on {}'.format(f1.health))

        f1_turn = not f1_turn

    if f1.health > 0:
        return 0
    else:
        return 1


def get_gold(item_set):
    cst = 0

    for i in item_set:
        cst += i.cost

    return cst


def do_battle(item_set):
    boss = Fighter(inp['Hit Points'], inp['Damage'], inp['Armor'])
    player = Fighter(100)
    for i in item_set:
        player.add_item(i)

    if fight(player, boss) == 0:
        return item_set
    else:
        return None

winning_sets = []
losing_sets = []
for i_set in item_sets:
    win_set = do_battle(i_set)

    if win_set is not None:
        winning_sets.append(win_set)
    else:
        losing_sets.append(i_set)

# winning_sets = sorted(winning_sets, key=lambda x: get_gold(x))
# for s in winning_sets:
#     print(get_gold(s), end=': ')
#     for i in s:
#         print(i, end=', ')
#     print()

losing_sets = sorted(losing_sets, key=lambda x: get_gold(x))
for s in losing_sets:
    print(get_gold(s), end=': ')
    for i in s:
        print(i, end=', ')
    print()