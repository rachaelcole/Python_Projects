# RTS game function using a file-based system of data storage - not scalable

class Knight(object):
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

class Archer(object):
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

class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == 'knight':
            return Knight(level)
        elif unit_type == 'archer':
            return Archer(level)

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit('knight', 1)
    archer1 = barracks.build_unit('archer', 2)
    print(f'[knight1]:\n{knight1}\n')
    print(f'[archer1]:\n{archer1}\n')



# Reference: 
# Badenhurst, Wessel. "Chapter 3: The Prototype Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 37-60.
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_3