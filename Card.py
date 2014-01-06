## @package Card
#  Definition of a card for the Cards simulation

no_suit=0
hearts=1
spades=2
diamonds=3
clubs=4

joker=0
ace=1
jack=11
queen=12
king=13

## Private implementation of the suit used in the card in order to avoid unneccessary comparison
#
class _Suit:
	def __init__(self, value=0):
		self.value = value
	def __eq__(self, other):
		return self.value == other.value
	def __str__(self):
		if(self.value == hearts):
			return "hearts"
		elif(self.value == spades):
			return "spades"
		elif(self.value == diamonds):
			return "diamonds"
		elif(self.value == clubs):
			return "clubs"
		else:
			return "no suit"

## Private implementation of a rank to be used in order to retain hard types
class _Rank:
	def __init__(self, value=0):
		self.value = value
	def __eq__(self, other):
		return self.value == other.value
	def __str__(self):
		if(self.value == joker):
			return "joker"
		elif(self.value == ace):
			return "ace"
		elif(self.value == jack):
			return "jack"
		elif(self.value == queen):
			return "queen"
		elif(self.value == king):
			return "king"
		else:
			return str(self.value)

## Public implementation of the card type
class Card:
	def __init__(self, suit =0, rank=0):
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