# Using the pythonic implementation of the observer pattern to implement our task tracking system

class Task(object):
    def __init__(self, user, _type):
        self.observers = set()
        self.user = user
        self._type = _type
    def register(self, observer):
        self.observers.add(observer)
    def unregister(self, observer):
        self.observers.discard(observer)
    def unregister_all(self):
        self.observers = set()
    def update_all(self):
        for observer in self.observers:
            observer.update(self)

class User(object):
    def __init__(self, wallet):
        self.wallet = wallet
        self.badges = []
        self.experience = 0
    def add_experience(self, amount):
        self.experience += amount
    def update(self, observed):
        self.add_experience(1)
    def __str__(self):      
        return "Wallet\t{}\nExperience\t{}\n+ Badges +\n{}\n++++++++++++++++".format(self.wallet, self.experience, '\n'.join([str(x) for x in self.badges]))

class Wallet(object):
    def __init__(self):
        self.amount = 0
    def increase_balance(self, amount):
        self.amount += amount
    def decrease_balance(self, amount):
        self.amount -= amount   
    def update(self, observed):
        self.increase_balance(5)    
    def __str__(self):
        return str(self.amount)

class Badge(object):
    def __init__(self, name, _type):
        self.points = 0
        self.name = name
        self._type = _type
        self.awarded = False
    def add_points(self, amount):
        self.points += amount
        if self.points > 3:
            self.awarded = True
    def update(self, observed):
        if observed._type == self._type:
            self.add_points(2)
    def __str__(self):
        if self.awarded:
            award_string = 'Earned'
        else:
            award_string = 'Not yet earned'
        return f'{self.name}: {award_string} [{self.points}]'


def main():
    wallet = Wallet()
    user = User(wallet)
    badges = [Badge('Fun Badge', 1), Badge('Bravery Badge', 2), Badge('Missing Badge', 3)]
    user.badges.extend(badges)
    tasks = [Task(user, 1), Task(user, 1), Task(user, 3)]
    for task in tasks:
        task.register(wallet)
        task.register(user)
        for badge in badges:
            task.register(badge)
    for task in tasks:
        task.update_all()
    print(user)


if __name__ == "__main__":
    main()





# Reference: 
# Badenhurst, Wessel. "Chapter 14: Observer Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 219-237,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_14.