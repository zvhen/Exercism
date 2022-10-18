"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    number_cards = ['2','3','4','5','6','7','8','9','10']
    face_cards = ['J','Q','K']
    if card == 'A':
        return 1
    elif card in face_cards:
        return 10
    elif card in number_cards:
        return int(card)
    else:
        raise ValueError('Card should only be from 2-10,A,J,Q or K and string format')

def higher_card(card_one, card_two):

    if value_of_card(card_two) == value_of_card(card_one):
        return card_one, card_two
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one

def value_of_ace(card_one, card_two):
    lower_limit = 10
    if card_one == 'A' or card_two == 'A':
        return 1
    elif (value_of_card(card_one)+value_of_card(card_two)) <= lower_limit:
        return 11
    else:
        return 1

def is_blackjack(card_one, card_two):
    if value_of_card(card_one)==10 and card_two == 'A':
        return True
    elif value_of_card(card_two)==10 and card_one =='A':
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    return (value_of_card(card_one)+value_of_card(card_two)) in range(9,12)

