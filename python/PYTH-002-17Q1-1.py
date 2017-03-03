# PYTH-002-17Q1-1
# A script to use Regular Expressions to validate a user's IPv4 Input

# START 3/3/17 @ 0417
# END 3/3/17 @ 0447

# Zero: Import Modules, describe program
# First: Prompt user for octets
# Second: Regex Validation
# Third: Output Result

import re	# Import the RegEx module for string searches

print('\n\n\n\n\nThis program uses Regular Expressions to Validate an IPv4 Address\n')
print('Please follow the prompts, pressing enter after each octet.\n\n')


############################################# Phase 1: Prompts

address = [1, 2, 3, 4]

for octet in range(0,4) :
	address[octet] = input('Please input the value of octet ' + str(octet + 1) + ' : ')


###... shit, realized true intention of this test, adding second method.
addressString = input('Please input an IPv4 Address for method 2 : ')



############################################# Phase 2: Regex Validation

validAddr = 1

pattern = re.compile("([0-2]?\d?\d\.){3}([0-2]?\d?\d){1}")
match = pattern.fullmatch(addressString)




############################################# Phase 3: Output
print(str(address))

if match:
	print("This is a valid IPv4 Address.")
else:
	print("This is --NOT-- a valid IPv4 Address.")
