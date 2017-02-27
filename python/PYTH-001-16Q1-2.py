# PYTH-001-16Q1-2
# Python Programming Challenge 001
# 2016 Quarter 1, second attempt

# Challenge: Given Linux's dictionary file and input of a pool of characters
#            Find the longest word that can be made with this pool of letters

# PREREQ - Python 3

# Import packages
import re

# Get user input, ensure valid input
matchtest = ''
while not matchtest:
	userInput = input('Please input a set of letters : ')

	# Validate Input, we asked for letters only.
	pattern = re.compile('^([A-Za-z])+$', re.IGNORECASE)
	matchtest = pattern.match(userInput)
	
	# DEBUG - test regex
	print('matchtest returned {}'.format(matchtest))

	# Ensure Input is lowercase for matching purposes
	userInput = userInput.lower()

	# save dictionary to variable
	dictFile = []
	dictFile.extend(open('/usr/share/dict/american-english-test'))

	# Iterate and Remove nonmatches
	pattern = re.compile('^([' + userInput + '])+$')
	resultFile = filter(pattern.match, dictFile)

	resultFinal = max(resultFile, key=len)
	
	# Output matches
	for word in resultFile:
		print('{}'.format(word))
	
	# DEBUG -  Print Result
	print('You typed {}'.format(userInput))
