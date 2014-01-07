## @package Common
#  Common and miscellanious functions
#
#  @author Kevin Wierman

## Provides a c-like enum for usage in other packages
#  @note Should anything else require this functionality, this should be moved to a common module
#  @warning This breaks forwards compatability with python 3.2
#  @param **enums the enumerated parameters, see Severity for usage
def enum(**enums):
	return type('Enum',(),enums)

## Provides the functionality for finding the average of a list of numerical values
def average(input_list=[]):
	return sum([float(x) for  x in input_list])/float(len(input_list))

## Provides the functionality for retrieving the standard deviation given the mean
def std_dev(input_list=[], mean=None ):
	if(type(mean)==type(None) ):
		mean=average(input_list)
	return sum( [abs( (float(x)-mean)*(float(x)-mean) ) for x in input_list  ] )/float(len( input_list))

## Provides a consice way of getting statistics
def get_stats(input_list=[]):
	mean= average(input_list)
	sd = std_dev(input_list, mean)
	return mean, sd