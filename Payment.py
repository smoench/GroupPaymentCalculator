__author__ = 'Simon Mönch'
__license__ = 'MIT'


class Payment:
    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount
        self.parties = []

    def add_partie(self, partie):
        self.parties.append(partie)

    def average(self):
        count = len(self.parties)
        return round(self.amount / count, 2)