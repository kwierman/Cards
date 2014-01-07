## @package Deck
#  Deck definition in the cards simulation

import Card

## Private implementation of the deck type in the cards simulation
class _Card_List:
	def __init__(self):
		self.cards = []
	def __str__(self):
		tmp_string = ""
		for i in self.cards:
			tmp_string+="\t"+str(i)+"\n"
		return tmp_string

## Class to represent decks of cards
class Deck:
	def __init__(self):
		self.private = _Card_List()

	## Checks to make sure card before adding in a card
	#  @param card the card that should be added to the deck
	def add_card(self, card ):
		if(not type(card) == type( Card.Card() ) ):
			raise TypeError("Function Requires input of Type \'Card\'")
		self.private.cards.append(card)

	## Appends other deck to this one
	def add_deck(self,other):
		for i in other.private.cards:
			self.add_card(i)

	## Removes a card from the deck
	#  @param card First instance of this card found in the deck will be removed
	def remove_card(self, card):
		self.private.cards.remove(card)

	## Check deck to see if it has a card
	#  @param self should be self explainatory
	#  @param card input the card you want to check against
	def has_card(self, card ):
		for i in self.private.cards:
			if( i == card ):
				return True
		return False
	def __str__(self):
		return "Deck:\n"+str(self.private)

	## For a given card, checks the deck for the card, then returns the card before
	def get_card_before(self, card):
		if(not type(card) == type(Card.Card() )):
			TypeError("Expected input of Type Card. Received: "+str(type(card) ) )
		before_card = Card.Card(0,0)
		for i in self.private.cards :
			if (i == card ):
				return before_card
			before_card = i
		return Card.Card(0,0)

	## For a given card, checks the deck for the card, then returns the card after
	def get_card_after(self, card):
		if(not type(card) == type(Card.Card() )):
			TypeError("Expected input of Type Card. Received: "+str(type(card) ) )
		found_card = False
		for i in self.private.cards :
			if(found_card):
				return i
			if(i==card):
				found_card = True
		return Card.Card(0,0)

## Constructs a deck in order determined by suit, rank
def construct_standard_deck():
	deck = Deck()
	for i in range(1,5):#suit
		for j in range(1,14):#rank
			deck.add_card( Card.Card(i,j) )
	return deck


