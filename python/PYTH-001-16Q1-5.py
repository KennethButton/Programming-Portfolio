# PYTH-001-17Q1-5.py
# Python Programming Exercise 001
# 1st Quarter of 2017
# Attempt 5 - No timer.
# Start: 0400 28/2/2017
# End:
# Duration:


################################################
# Methodology Used
#
# Section 1: User Input and Sterilization
# Section 2: Dictionary Loading
# Section 3: Optimizations
# Section 4: Solving
# Section 5: Display Output
################################################

# Import Required Packages
import re

# Debug mode, 0 is off. 1 is active
DEBUG = 0

# Initialize Lists
dictionary = []
results = []

# Dictionary Source to use
dictToUse = '/usr/share/dict/american-english-test'




################################################
# SECTION 1: User Input
################################################

print ('\n\n\n\n\n\n\n\n\n\n\n')
inputString = input('''---- This program finds the largest word possible from
a set of letters provided. It does this by using the dictionary file, assuming
the user is using Ubuntu Linux 16.04 and compatable systems.

Please Input a set of letters to find a word for: ''')

# Lowercase it to make easier to work with
inputString = inputString.lower()




################################################
# SECTION 2: Dictionary Loading
################################################

print('\n\n >>> Loading Dictionary')

# Open file for reading
if DEBUG == 1:
	dictHandle = open('./american-english-test')
else:
	dictHandle = open(dictToUse)
dictionary.extend(dictHandle)
dictHandle.close()



################################################
# SECTION 3: Optimizations - Optional
################################################

print('\n\n >>> Optimizing Search')

# For display and search purposes, strip the trailing \n
## TODO: Figure out how to do this later. nonessential
for word in dictionary:
	word.replace('\n','')




################################################
# SECTION 4: Solving
################################################

print('\n\n >>> Searching For Results')

# For each word in the dictionary, test each letter against the
# Search requirements. If there is a match, notate it, continue
# checking. If the number of letters that matched search equal
# the letters in the word, add that to the results table.
for word in dictionary:
	lettersMatched = 0

	# DEBUG: Show Word being checked
	if DEBUG == 1:
		print('Now checking: ' + word)

	for letterInWord in range(0, len(word)-1):
		for letterInSearch in range(0,len(inputString)):
			
			# DEBUG: Show Letter comparison being made
			if DEBUG == 1:
				print('>> is "{0}" the same as  "{1}"?'.format(word[letterInWord].lower(), inputString[letterInSearch]))

			if word[letterInWord].lower() == inputString[letterInSearch]:
				# DEBUG: Show confirmation of match
				if DEBUG == 1:
					print('>>>>>>>>>>>>>>>>>>>>> MATCH FOUND <<<<<<<<<<<<<<<<<')
				lettersMatched = lettersMatched + 1
				break
	if lettersMatched == len(word)-1:
		results.append(word)
		# DEBUG: Show Success of Match
		if DEBUG == 1:
			print('^#$%^#$%^#$%^#  MATCH SUCCESSFUL $@$%@#$%@#$%@#$%\n\n\n\n\n\n')
	else:
		# DEBUG: Show Failure of Match
		if DEBUG == 1:
			print('MATCH FAILED WITH ONLY {0} OUT OF {1} MATCHING.'.format(lettersMatched, len(word)))


################################################
# SECTION 5: Display Output
################################################

print('''\n\n------------------------------------------\n\n\n
For your search query of {0},
The Longest Word(s) found:'''.format(inputString))

# Handle No Results
if len(results) <= 0:
	print('''

	''')
	print(" >>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<< ")
	print(" >>> Your Letters Provided No Results <<< ")
	print(" >>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<< ")

else:
	print(" Largest word is {0}".format(max(results, key = len)))

	for word in results:
		print('{}'.format(word))
