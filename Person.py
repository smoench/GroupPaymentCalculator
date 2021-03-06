__author__ = 'Simon Mönch'
__license__ = 'MIT'


class Person:
    def __init__(self, name):
        self.name = name
        self.pays = {}

    def __repr__(self):
        return self.name

    def paid(self, person, amount):
        if person in self.pays:
            self.pays[person] += amount
        else:
            self.pays[person] = amount

    def owes(self, person, amount):
        if person in self.pays:
            self.pays[person] -= amount
        else:
            self.pays[person] = -1 * amount