from OOP_multiple_instances import PartyAnimal              # import class from .py file


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(f'{self.name} points: {self.points}')


s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
# print(dir(j))

