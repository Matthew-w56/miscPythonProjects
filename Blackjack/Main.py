__author__ = 'Matthew Williams'
# Started on 11/4/16

from random import randint
from CardList import *
from Functions import *

print('Welcome!  Enjoy your game of BlackJack!')
print('The goal of the game is to take cards')
print('And get as close to a sum total of 21 as')
print('You can without going above 21 at all!')
print('')
print('Let\'s Start.')
print('')

hit_cards = []

card1 = pick_card()
card2 = pick_card()

hit_cards.append(card1)
hit_cards.append(card2)

card1.write()
card2.write()

fill()
total = card1.value + card2.value
hitting = True

if total == 21:
    print('Lucky you! You got a BlackJack!')
    hitting = False

while hitting:
    print('Your total so far is: ' + str(total))
    new = input('Do you want another card? (Y|N) > ')
    fill()
    if new == 'N':
        hitting = False
        print('Your final score is ' + str(total))
    elif new == 'Y':
        new_card = pick_card()
        hit_cards.append(new_card)
        new_card.write()
        total += new_card.value

        if total > 21:
            fill()
            for card in hit_cards:
                if 'Ace of ' in card.name:
                    card.value = 1
                    total = 0
                    for x in hit_cards:
                        total += x.value
            if total > 21:
                print('You busted!  Your final score is ' + str(total))
                hitting = False
        elif total == 21:
            fill()
            print('BlackJack! You got 21!')
            hitting = False
    fill()