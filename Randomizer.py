## @package Randomizer
#  Routines for producing random number quantites
#  @author Kevin Wierman

import random

import Card
import Deck

## Generates random Card
def generate_random_card():
	suit=random.randint(1,4)
	rank=random.randint(1,13)
	return Card.Card(suit,rank)

## Generates random deck in worst order time
def random_deck():
	deck = Deck.Deck()
	for i in range(52):#create a 52 card deck
		card = generate_random_card()
		while( deck.has_card(card) ):
			card = generate_random_card()
		deck.add_card( card ) 
	return deck

## Generates a mapping for the tent shuffle
def tent_map():
	output=[]
	while(True):
		output.append( random.randint(1,4) )
		output_sum=0
		for i in output:
			output_sum+=i
		if(output_sum>48):
			output.append(52-output_sum )
			break
	return output

## Generates a split point roughly somewhere in the middle of the deck
# @note: Needs improvement for normal distribution around deck center
def split_point():
	return random.randint(24,28)

## Generates a random boolean quantitity for shuffling purposes
# @note: this is also done in worst order time.
def shuffle_left():
	tmp_rand = random.randint(1,2)
	return tmp_rand==1