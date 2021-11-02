# Simple RTS using unit classes with a unit_type attribute and a Barracks class containing a build_unit() method

class Knight(object):
    def __init__(self, level):
        self.unit_type = "knight"
        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 1
            self.weapon = "short sword"
        elif level == 2:
            self.life = 400
            self.speed = 5
            self.attack_power = 6
            self.attack_range = 2
            self.weapon = "long sword"
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack power: {self.attack_power}\nAttack range: {self.attack_range}\nWeapon: {self.weapon}"

class Archer(object):
    def __init__(self, level):
        self.unit_type = "archer"
        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "short bow"
        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 3
            self.attack_range = 10
            self.weapon = "long bow"
    def __str__(self):
        return f"Type: {self.unit_type}\nLife: {self.life}\nSpeed: {self.speed}\nAttack power: {self.attack_power}\nAttack range: {self.attack_range}\nWeapon: {self.weapon}"

class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == "knight":
            return Knight(level)
        elif unit_type == "archer":
            return Archer(level)

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("archer", 2)
    print(f'[knight1]:\n{knight1}')
    print(f'[archer1]:\n{archer1}')



# Reference: 
# Badenhurst, Wessel. "Chapter 3: The Prototype Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 37-60.
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_3