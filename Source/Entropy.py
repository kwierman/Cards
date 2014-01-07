## @package Entropy
# This is a package for defining the entropic distance one deck is from another


import Deck
import Card

def deck_entropy(deck_1, deck_2 = Deck.construct_standard_deck()):
	total=0
	for i, card in enumerate(deck_1):
		diff = 0
		for j, compare in enumerate(deck_2):
			if(card==compare):
				diff == i-j
				if(diff<0):
					diff*=(-1)
		total+=diff
	return total
