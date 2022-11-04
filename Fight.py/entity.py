from items import *

class Entity:
    def __init__(self, name, force, defense, hp):
        self.name = name
        self.inventory = []
        self.critical_chance = 0
        self.force = force
        self.defense = defense
        self.hp = hp

    def damage(self, damage_amount, attacker):
        if (damage_amount > self.hp):
            overkill = abs(self.hp - damage_amount)
            self.hp = 0
            if (overkill > 0):
                print("{0} takes fatal damage from {1}, with {2} overkill!"
                      .format(self.name.capitalize(), attacker, overkill))
            else:
                print("{0} takes fatal damage from {1}!"
                      .format(self.name.capitalize(), attacker))
        else:
            self.hp -= damage_amount
            print("{0} takes {1} damage from {2}!"
                  .format(self.name.capitalize(), damage_amount, attacker))


class monster(Entity):
    def __init__(self, name):
        if name == "gobelin":
            super().__init__("gobelin", 3, 3, 10)
        elif name == "dragon":
            super().__init__("dragon", 50, 50, 100)
        elif name == "loup":
            super().__init__("loup", 10, 15, 50)
        self.wins = 0


class Player(Entity):
    def __init__(self, name, adventurer_type):
        self.name = name
        self.adventurer_type = adventurer_type
        self.equipped_weapon = None
        self.quest_list = []
        self.wins = 0
        if adventurer_type == "Warrior":
            super().__init__(name, 30, 20, 10)
            self.inventory.append(weapon("Sword", 10, 5))
            self.inventory.append(protection_wand("Wand Sword", 20, 5, 10))
        elif adventurer_type == "Wizard":
            super().__init__(name, 20, 30, 10)
            self.inventory.append(weapon("Staff", 3, 50))
            self.inventory.append(weapon("Giant Sword", 40, 5))
