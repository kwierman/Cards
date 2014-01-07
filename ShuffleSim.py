## @mainpage Cards
#  @tableofcontents
#  @section intro Introduction
#
#  The Cards simulation was created for an easy way to simulate card games and calculate probabilities associated with cards.
#
#  The primary packages to be used are:
#    - Card
#      - Card class definitions
#    - Deck
#      - Deck class definitions
#    - Shuffle
#      - Shuffling algorithms
#    - Randomizer
#      - Randomization routines
#
#  @section downloading Downloading
#  The following code can be used to download the code:
#  ~~~~~~~~~~~~~~~~~~~~~
#  git clone https://github.com/kwierman/Cards.git
#  ~~~~~~~~~~~~~~~~~~~~~
#
#  @section dependencies Dependencies
#  This package depends on:
#    - Python 2.7 (Python 3.2 is unsupported at this point)
#    - ROOT
#      - <a href="http://root.cern.ch/drupal/">ROOT Website</a>
#      - PyROOT must be enabled in the ROOT build.
#      - The PYTHONPATH environment variable must be set to the PyROOT directory 

## @file ShuffleSim.py
#  This is an example simulation card that uses the Cards library to simulate the shuffling of cards and calculates the probability of pattern retention

import Deck
import Entropy
import Randomizer
import DeckCounter
import Shuffle
import Log

from array import *

try:
	from ROOT import *
except:
	from ROOT import *

def main():
	Log.set_logger_file("debug.txt")

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
	n_iterations = 10000
	n_shuffles = 20
	Log.log(Log.Severity.Header, "Creating Random Decks")
	deck_list = [Randomizer.random_deck()  for i in range(n_iterations)]
	Log.log(Log.Severity.OK, "Done")
	Log.log(Log.Severity.Header, "Creating maps")
	mapping = [ DeckCounter.generate_map(i) for i in deck_list ]
	Log.log(Log.Severity.OK, "Done")
	for i in range(n_shuffles):
		Log.log(Log.Severity.Normal, "Shuffling: "+str(i+1) )
		split_points = [Randomizer.split_point() for j in range(n_iterations) ]
		tent_maps = [Randomizer.tent_map() for j in range(n_iterations) ]
		shuffle_direction = [Randomizer.shuffle_left() for j in range(n_iterations)]
		deck_list[:] = [Shuffle.tent_shuffle(deck_list[j], split_points[j], tent_maps[j],shuffle_direction[j]  ) for j in range(n_iterations) ]
		similarities = [DeckCounter.number_of_matching_cards(deck_list[j], mapping[j] ) for j in range(n_iterations) ]
		Log.log(Log.Severity.OK, "Done")

		mean,err = Common.get_stats(similarities)
		Log.log(Log.Severity.Normal," Mean: "+str(mean)+"+/-"+str(err))
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