class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(f'{self.name} party count is {self.x}')

"""

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()

"""
