"""
In the prototype pattern, we favour composition over ingeritance. We want to use a clone() method on the object 
instance that we want to copy, which clones the object and then modifies its values. The three components needed
for the prototype pattern are:
    - Client creates a new object by asking a prototype to clone itself
    - Prototype declares an interface for cloning itself
    - Concrete prototype implements the operation for cloning itself

In our RTS example, every building should keep a list of the prototypes that it can use to build units, with properties
to match the current state of the building. When a building is upgraded, this list is updated to reflect its new 
capabilities (stronger units).
"""

from prototype_1 import Prototype
from copy import deepcopy

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = 'knight'
        filename = f'{self.unit_type}_{level}.txt'
        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack power: {self.attack_power}\nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = 'archer'
        filename = f'{self.unit_type}_{level}.txt'
        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack power: {self.attack_power}\nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    def clone(self):
        return deepcopy(self)

class Horseman(Prototype):
    def __init__(self, level):
        self.unit_type = 'horseman'
        filename = f'{self.unit_type}_{level}.txt'
        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack power: {self.attack_power}\nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    def clone(self):
        return deepcopy(self)

class Warrior(Prototype):
    def __init__(self, level):
        self.unit_type = 'warrior'
        filename = f'{self.unit_type}_{level}.txt'
        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack power: {self.attack_power}\nAttack range: {self.attack_range}\nWeapon: {self.weapon}"
    def clone(self):
        return deepcopy(self)

class Barracks(object):
    def __init__(self):
        self.units = {
            'warrior': {
                1: Warrior(1),
                2: Warrior(2)
            },
            'archer': {
                1: Archer(1),
                2: Archer(2)
            }
        }
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()

class Stable(object):
    def __init__(self):
        self.units = {
            'knight': {
                1: Knight(1),
                2: Knight(2)
            },
            'horseman': {
                1: Horseman(1),
                2: Horseman(2)
            }
        }
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":

    barracks = Barracks()
    stable = Stable()

    warrior1 = barracks.build_unit('warrior', 1)
    archer1 = barracks.build_unit('archer', 2)
    knight1 = stable.build_unit('knight', 1)
    horseman1 = stable.build_unit('horseman', 2)

    print(f'[warrior1]:\n{warrior1}\n')
    print(f'[archer1]:\n{archer1}\n')
    print(f'[knight1]:\n{knight1}\n')
    print(f'[horseman1]:\n{horseman1}\n')




# Reference: 
# Badenhurst, Wessel. "Chapter 3: The Prototype Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 37-60.
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_3