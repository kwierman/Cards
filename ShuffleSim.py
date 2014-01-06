#/usr/bin/python
#ShuffleSim.py

import Deck
import Entropy
import Randomizer
import DeckCounter
import Shuffle

from array import *

try:
	from ROOT import *
except:
	from ROOT import *

def main():

	shuffles=[]
	entropy=[]

	for j in range(100):
		deck_1 = Randomizer.random_deck() #creates an empty randomized deck
		mapping = DeckCounter.generate_map(deck_1)
		mapped_deck   =  DeckCounter.generate_map(deck_1)
		deck_2 = deck_1

		for i in range(20):
			split_point = Randomizer.split_point()
			tent_map = Randomizer.tent_map()
			deck_2 = Shuffle.tent_shuffle(deck_2, split_point, tent_map, Randomizer.shuffle_left() )
			entropic_similarity = DeckCounter.number_of_matching_cards(deck_2, mapping )


			#print sum(DeckCounter.position_difference(deck_1, deck_2) )
			shuffles.append(i)
			#entropy.append( sum(DeckCounter.position_difference(deck_1, deck_2) ) )
			entropy.append( entropic_similarity )

	canvas = TCanvas()
	x_array = array('i',shuffles)
	y_array = array('i',entropy)
	newGraph = TGraph(len(shuffles),x_array, y_array )   
	newGraph.SetMarkerColor(2)
	newGraph.SetMarkerStyle(21)
	newGraph.Draw("AP")
	newGraph.SetTitle("Shuffle Entropic Evolution")
	newGraph.GetXaxis().SetTitle("Shuffles from Generated Deck")
	newGraph.GetYaxis().SetTitle("Entropic Value")
	canvas.Update()
	canvas.SaveAs("1.eps")

	#now for the second iteration of the simulation
	c2 = TCanvas()
	shuffle_list =[]
	mean_list=[]
	err_list=[]
	zero_list=[]

	deck_list =[]
	n_iterations = 1000
	n_shuffles = 20
	deck_list = [Randomizer.random_deck()  for i in range(n_iterations)]
	mapping = [ DeckCounter.generate_map(i) for i in deck_list ]
	for i in range(n_shuffles):
		split_points = [Randomizer.split_point() for j in range(n_iterations) ]
		tent_maps = [Randomizer.tent_map() for j in range(n_iterations) ]
		shuffle_direction = [Randomizer.shuffle_left() for j in range(n_iterations)]
		deck_list[:] = [Shuffle.tent_shuffle(deck_list[j], split_points[j], tent_maps[j],shuffle_direction[j]  ) for j in range(n_iterations) ]
		similarities = [DeckCounter.number_of_matching_cards(deck_list[j], mapping[j] ) for j in range(n_iterations) ]

		mean = float(sum(similarities) )/float(len(similarities))
		err = sum( [abs( (float(x)-mean)*(float(x)-mean) ) for x in similarities  ] )/float(len( similarities))
		print "Shuffle: "+str(i)+" Mean: "+str(mean)+"+/-"+str(err)
		shuffle_list.append(i+1)
		mean_list.append(mean)
		err_list.append(err)
		zero_list.append(0)

	x_array = array('d',shuffle_list)
	x_err = array('d', zero_list)
	y_array = array('d',mean_list)
	y_err = array('d', err_list)
	errGraph = TGraphErrors(len(shuffle_list), x_array, y_array, x_err, y_err)
	errGraph.SetMarkerColor(4)
	errGraph.SetMarkerStyle(7)
	errGraph.Draw("APL")
	errGraph.SetTitle("Shuffle Pattern Evolution")
	errGraph.GetXaxis().SetTitle("Shuffles from Initial Deck")
	errGraph.GetYaxis().SetTitle("Number of Pattern Matching Similarities")
	c2.Update()
	c2.SaveAs("2.eps")


	import time
	time.sleep(30)

if __name__ == "__main__":
	main()