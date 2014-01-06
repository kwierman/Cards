## @package DeckCounter
#  This adds in the functionality to count the number of cards adjascent in a deck

import Deck

## This will return a map of adjascent cards
#  @param deck, the reference deck to be used in the generation
#  @return list of tuples containing cards
def generate_map(deck = Deck.Deck() ):
	# for each card, it will
	output = []
	for card in deck.private.cards:
		before = deck.get_card_before( card)
		mapped = (card, deck.get_card_before( card ), deck.get_card_after( card ) )
		output.append( mapped) 
	return output


## Returns the absolute difference in position of cards in two decks
#  @param deck1 reference deck
#  @param deck2 difference deck
#  @return list of position differences
def position_difference(deck1, deck2):
	output=[]
	for i, card1 in enumerate(deck1.private.cards):
		position_difference=0
		for j, card2 in enumerate(deck2.private.cards):
			if(card1==card2):
				position_difference=i-j
		output.append( abs(position_difference) )
	return output

## Returns the number of card patterns matching the generated map:
def number_of_matching_cards(deck=Deck.Deck(), mapping = generate_map(Deck.Deck() )):
	output=0
	for i in deck.private.cards:
		card_before = deck.get_card_before(i)
		card_after = deck.get_card_after(i)
		for j in mapping:
			if( j[0]==i and card_before ==j[1] and card_after == j[2] ):
				output+=1
	return output


if __name__ == "__main__":
	deck = Deck.construct_standard_deck()
	print deck
	mapped_deck = generate_map(deck )
	print mapped_deck