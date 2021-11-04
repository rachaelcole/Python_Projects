# Observer pattern

# Take an example system where users can complete tasks. Users receive points upon challenge completion and general EXP 
# points and skill points for the skills used to complete each task. We need to keep track of user credits earnt/spent, the
# EXP the user has accumulated, and the scores that count toward earning specific badges/achievements. The following code
# is a non-scalable, tightly coupled system that can be improved upon.

class Task(object):
    def __init__(self, user, _type):
        self.user = user
        self._type = _type
    
    def complete(self):
        self.user.add_experience(1)
        self.user.wallet.increase_balance(5)

        for badge in self.user.badges:
            if self._type == badge._type:
                badge.add_points(2)


class User(object):
    def __init__(self, wallet):
        self.wallet = wallet
        self.badges = []
        self.experience = 0
    
    def add_experience(self, amount):
        self.experience += amount
    
    def __str__(self):
        return "Wallet\t{}\nExperience\t{}\n+ Badges +\n{}\n++++++++++++++++".format(self.wallet, self.experience, '\n'.join([str(x) for x in self.badges]))


class Wallet(object):
    def __init__(self):
        self.amount = 0

    def increase_balance(self, amount):
        self.amount += amount
    
    def decrease_balance(self, amount):
        self.amount -= amount
    
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
    
    def __str__(self):
        if self.awarded:
            award_string = 'Earned'
        else:
            award_string = 'Not yet earned'
        return f'{self.name}: {award_string} [{self.points}]'


def main():
    wallet = Wallet()
    user = User(wallet)

    user.badges.append(Badge('Fun Badge', 1))
    user.badges.append(Badge('Bravery Badge', 2))
    user.badges.append(Badge('Missing Badge', 3))

    tasks = [Task(user, 1), Task(user, 1), Task(user, 3)]
    for task in tasks:
        task.complete()
    
    print(user)


if __name__ == "__main__":
    main()




# Reference: 
# Badenhurst, Wessel. "Chapter 14: Observer Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 219-237,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_14.