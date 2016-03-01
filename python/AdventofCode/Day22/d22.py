#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "d22.py", "22/12/2015", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)


inp = {
    'Hit Points': 71,
    'Damage': 10,
    'Armor': 0
}


class Spell(object):
    def __init__(self, name, cst, dmg, heal, efct):
        self.name = name
        self.cost = cst
        self.damage = dmg
        self.heal = heal
        self.effect = efct

    def __str__(self):
        return "{}: cost({}), dmg({}), heal({})".format(self.name, self.cost, self.damage, self.heal)

spells = [Spell('Magic Missile', 53, 4, 0, None),
          Spell('Drain', 73, 2, 2, None),
          Spell('Shield', 113, 0, 0, ('Shield', 6, 7)),
          Spell('Poison', 173, 0, 0, ('Poison', 6, 3)),
          Spell('Recharge', 229, 0, 0, ('Recharge', 5, 101))
          ]


class Fighter(object):
    def __init__(self, hp, mana=0, dmg=0, arm=0):
        self.health = hp
        self.mana = mana
        self.damage = dmg
        self.armor = arm

        self.effects = []

    def add_effect(self, spll):
        for e in self.effects:
            if e[1] > 0:
                if e[0] == spll[0]:
                    return
                else:
                    self.effects.append(list(spll))

    def effect_tick(self):
        for e in self.effects:
            if e[1] > 0:
                e[1] -= 1
                if e[0] == 'Poison':
                    self.health -= e[2]
                elif e[0] == 'Recharge':
                    self.mana += e[2]

    def take_damage(self, attack, magic=False):
        if not magic:
            attack -= self.armor
            for e in self.effects:
                if e[0] == 'Shield' and e[1] > 0:
                    attack -= e[2]
                    break
        self.health -= max(1, attack)

    def __str__(self):
        return "HP: {}, DMG: {}, ARM: {}".format(self.health, self.damage, self.armor)


def fight(player, boss, p_turn=True):
    player.effect_tick()
    boss.effect_tick()
    if player.health < 0 or player.mana < min(spells, key=lambda x: x.cost):
        pass



# def fight(player, boss):
#     player_turn = True
#     while player.health > 0 and boss.health > 0:
#
#         if player_turn:
#             boss.take_damage(player.damage)
            # pass
            # print('boss on {}'.format(boss.health))
        # else:
        #     player.take_damage(boss.damage)
        #     print('player on {}'.format(player.health))
        #
        # player_turn = not player_turn
    #
    # if player.health > 0:
    #     return 0
    # else:
    #     return 1


# def do_battle(item_set):
    # boss = Fighter(inp['Hit Points'], inp['Damage'], inp['Armor'])
    # player = Fighter(100)
    # for i in item_set:
        # player.add_item(i)
    #
    # if fight(player, boss) == 0:
        # return item_set
    # else:
        # return None
#
# winning_sets = []
# losing_sets = []
# for i_set in item_sets:
#     win_set = do_battle(i_set)
#
#     if win_set is not None:
#         winning_sets.append(win_set)
#     else:
#         losing_sets.append(i_set)