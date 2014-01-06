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