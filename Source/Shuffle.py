""" @package Shuffle
	Performs shuffling operations on decks
"""

import Deck
## splits the deck into two decks
#  @param deck The deck to be split
#  @param split_point how many cards from the top of the deck to split it
def split_deck(deck, split_point=26):
	deck_1 = Deck.Deck()
	deck_2 = Deck.Deck()
	for x, card in enumerate(deck.private.cards):
		if(x<split_point):
			deck_1.add_card(card)
		else:
			deck_2.add_card(card)
	return (deck_1, deck_2)

## performs a tent shuffle
def tent_shuffle(deck, split_point=26, groups=[], shuffle_left=True):
	#first split it into two decks
	deck1, deck2 = split_deck( deck, split_point )
	if(shuffle_left):
		deck3=deck1
		deck1=deck2
		deck2=deck3
	#for each of the groups of cards
	result_deck=Deck.Deck()
	for x,i in enumerate(groups):
		tent_group=Deck.Deck()
		if(x%2==0 ):
			tent_group,deck1 = split_deck(deck1, i)
		else:
			tent_group,deck2 = split_deck(deck2, i)
		result_deck.add_deck(tent_group)
	result_deck.add_deck(deck1)
	result_deck.add_deck(deck2)
	return result_deck
	