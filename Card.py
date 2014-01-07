## @package Card
#  Definition of a card for the Cards simulation
#
#  @author Kevin Wierman

import Common

## Defines the numerical values for card suits.
#  The Ranking is as follows:
#    0. Non-suit type for null-cards (value=Suits.no_suit)
#    1. Hearts (value=Suits.hearts)
#    2. Spades (value=Suits.spades)
#    3. Diamonds (value=Suits.diamonds)
#    4. Clubs (value=Suits.clubs)
Suits = Common.enum(no_suit=0,hearts=1,spades=2,diamonds=3,clubs=4)
Ranks = Common.enum(joker=0,ace=1,jack=11,queen=12,king=13)

## Private implementation of the suit used in the card in order to avoid unneccessary comparison
#
class _Suit:
	## Default behavior is to 
	def __init__(self, value=Suits.no_suit):
		self.value = value
	def __eq__(self, other):
		return self.value == other.value
	## String representation is in the format: "<value>"
	def __str__(self):
		if(self.value == Suits.hearts):
			return "hearts"
		elif(self.value == Suits.spades):
			return "spades"
		elif(self.value == Suits.diamonds):
			return "diamonds"
		elif(self.value == Suits.clubs):
			return "clubs"
		else:
			return "no suit"

## Private implementation of a rank to be used in order to retain hard types
class _Rank:
	def __init__(self, value=Ranks.joker):
		self.value = value
	def __eq__(self, other):
		return self.value == other.value
	## String representation is in the format: "<value>".
	#  <value> can take on either numerical values or string representation for face cards.
	#  Default behavior for numerical values beyond the normal card system is to evaluate to "joker".
	def __str__(self):
		if(self.value == Ranks.joker):
			return "joker"
		elif(self.value == Ranks.ace):
			return "ace"
		elif(self.value == Ranks.jack):
			return "jack"
		elif(self.value == Ranks.queen):
			return "queen"
		elif(self.value == Ranks.king):
			return "king"
		else:
			return str(self.value)

## Public implementation of the card type
class Card:
	def __init__(self, suit =Suits.no_suit, rank=Ranks.joker):
		self.suit = _Suit(suit)
		self.rank = _Rank(rank)

	def get_suit(self):
		return self.suit.value

	def get_rank(self):
		return self.rank.value

	def __eq__(self,other):
		return self.rank == other.rank and self.suit == other.suit 

	def __repr__(self):
		return "Card: "+str(self.rank)+"  \tof  \t"+str(self.suit)