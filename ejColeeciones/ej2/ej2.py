from card import Card
import random

PALO = "BASTOS COPAS ESPADAS OROS".split()
NUMERO = "AS 2 3 4 5 6 7 SOTA CABALLO REY".split()
NUM_CARD = 5

num_cards_generated = 0
cards_in_set = set()
while num_cards_generated != NUM_CARD:
    num_cards_generated += 1
    card = Card(random.choice(NUMERO), random.choice(PALO))
    cards_in_set.add(card)

cards_in_list = list(cards_in_set)
cards_in_list.sort(key=lambda x: (x.suit, NUMERO.index(x.number)))  # lambda sirve para ordenar la lista según tu le indiques
