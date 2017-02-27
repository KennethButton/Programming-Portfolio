# PYTH-001-16Q1-3
# Third attempt, no regex.

# Get User Input
userInput = input('Please enter your letters : ')
userInput = userInput.toLower()

# Get Dictionary
dictFile = open('/usr/share/dict/american-english-test')
dictResults = []
dictResults.extend(dictFile)
dictFile.close()

# Cull impossible entries to prevent excessive iterations

## METHOD 1: Length check.
inputLength = len(userInput)
for word in dictResults:
	if len(word)-1 > inputLength: #account for the crlf at the end
		dictResults.remove(word)

## METHOD 2: Character existence check
#for word in dictResults:
#	for x in range(0, len(word)-1)
#		if userInput[x:] in word:



# Print possible options remaining
resultsFile = open('./results.txt', 'w')
for word in dictResults:
	resultsFile.write(word)
resultsFile.close()

# Print longest word
print(max(dictResults, key=len))
