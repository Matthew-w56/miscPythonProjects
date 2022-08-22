from CardList import *
from random import randint


class NewCard(object):
    def __init__(self, c):
        self.name = Card_Names[c]
        self.value = Cards[self.name]

    def write(self):
        print(self.name)


def pick_card():
    n = Availables.pop(randint(0, len(Availables) - 1))
    return NewCard(n)


def fill():
    print('')