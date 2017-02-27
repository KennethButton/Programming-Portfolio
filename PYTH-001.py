# PYTH-001
# A script to figure what is the largest word that can be made with letters provided.


# Zero: Import Modules to be used
# First: Prompt user for letters to use
# Second: Sanitize input using REGEX
# Third: Do search using REGEX by loading file
# Fourth: Iterate through list to find longest value


import re #import the regular expressions module for ease of string searches

# Phase 1 - Prompt user for letters to use
print('Please input a string of letters to use, spaces are not required:')

searchfor = 'ypthNO'
lengthInput = len(searchfor);

# Phase 2 - Sanitize Input
searchfor = searchfor.lower()
print('You were searching for: ' + searchfor)

# Phase 3 - Load file, run regex on it.
dictFile = open('/usr/share/dict/american-english-test')

words = []
words.extend(dictFile)

# Phase 4 - Iterate to find longest

## Do it in one pass, instead of running optimization runs first.



## Output Remaining list
print('The Words that you can choose from are: ')

for word in words:
	print(word)
	if word == '':
		break

print('AND WE ARE DONE')
