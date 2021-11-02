"""
Using the Prototype design pattern

Suppose we have a RTS game where a player wants to build Knights. Knights can only be built in Barracks
buildings. A player can have more than one Barracks building, to spawn Knights faster.

We could define a Barracks class that has a generate_knight method that returns a Knight object, which 
is an instance of the Knight class. The Knight class will have basic properties:
    - Life
    - Speed
    - Attack power
    - Attack range
    - Weapon

The files in this chapter explore some sub-optimal designs for an RTS game implementation as described above, and
then explores a prototype design pattern to optimise.
"""

# Simple RTS using separate classes for units

class Knight(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Knight"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon
    
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}"

class Archer(object):
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Archer"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack Power: {self.attack_power}\nAttack Range: {self.attack_range}\nWeapon: {self.weapon}"


class Barracks(object):
    def generate_knight(self):
        return Knight(400, 5, 3, 1, "short sword")
    
    def generate_archer(self):
        return Archer(250, 8, 2, 2, "bow and arrow")

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer1 = barracks.generate_archer()
    print(f"[Knight 1]:\n{knight1}")
    print(f"[Archer 1]:\n{archer1}")



# Reference: 
# Badenhurst, Wessel. "Chapter 3: The Prototype Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 37-60.
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_3