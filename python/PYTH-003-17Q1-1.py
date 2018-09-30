# PYTH-003-17Q1-1
# INT to String

# A function that returns the lexical value of a single digit
def DigitToString (Digit, Caps = False, Teens = False ):
	# Check to see if value is indeed a digit
	# TODO: Actually create this check

	if Caps:
		if Digit == 1:
			return "One"
		elif Digit == 2:
			return "Two"
		elif Digit == 3:
			return "Three"
		elif Digit == 4:
			return "Four"
		elif Digit == 5:
			return "Five"
		elif Digit == 6:
			return "Six"
		elif Digit == 7:
			return "Seven"
		elif Digit == 8:
			return "Eight"
		elif Digit == 9:
			return "Nine"
		elif Digit == 0:
			return "Zero"
		else:
			return "Not a digit"
	else:
		if Digit == 1:
			return "one"
		elif Digit == 2:
			return "two"
		elif Digit == 3:
			return "three"
		elif Digit == 4:
			return "four"
		elif Digit == 5:
			return "five"
		elif Digit == 6:
			return "six"
		elif Digit == 7:
			return "seven"
		elif Digit == 8:
			return "eight"
		elif Digit == 9:
			return "nine"
		elif Digit == 0:
			return "zero"
		else:
			return "not a digit"


# Returns a digitgroup value (expects 3 digits), that is to be affixed with a suffix
# like (thousand, million, etc.) after this function is called
def DigitgroupToString (DigitGroup, Caps = False):
	returnString = ""

	if DigitGroup > 999:
		return "Value is larger than a single digit group"
	elif DigitGroup < 0:
		return "This function doesn't handle negative numbers"
	elif DigitGroup >= 100:
		returnString = returnString + DigitToString(DigitGroup[0]) + "-hundred"
	
	LastTwo = str(DigitGroup).zfill(3)[1:2]
	NumLastTwo = int(LastTwo)

	if NumLastTwo < 11:
		return DigitToString(DigitGroup, Caps)
	elif NumLastTwo < 20:
		if NumLastTwo == 11:
			return "eleven"
		elif NumLastTwo == 12:
			return "twelve"
		elif NumLastTwo == 13:
			return "thirteen"
		elif NumLastTwo == 14:
			return "fourteen"
		elif NumLastTwo == 15:
			return "fifteen"
		elif NumLastTwo == 16:
			return "sixteen"
		elif NumLastTwo == 17:
			return "seventeen"
		elif NumLastTwo == 18:
			return "eighteen"
		elif NumLastTwo == 19:
			return "nineteen"
		else:
			return ">> DigitgroupToString Error: Digitgroup < 20, yet out of range"
	elif NumLastTwo <= 99:
		# search to find prefix
		if NumLastTwo <= 29:
			returnString = "twenty"
		elif NumLastTwo <= 39:
			returnString = "thirty"
		elif NumLastTwo <= 49:
			returnString = "fourty"
		elif NumLastTwo <= 59:
			returnString = "fifty"
		elif NumLastTwo <= 69:
			returnString = "sixty"
		elif NumLastTwo <= 79:
			returnString = "seventy"
		elif NumLastTwo <= 89:
			returnString = "eighty"
		elif NumLastTwo <= 99:
			returnString = "ninety"
		else:
			returnString = ">> DigitgroupToString Error: Digitgroup <= 99"
	return returnString


print('\n\n\nDigit To String Testing\n')
print('1 - ' + DigitToString(1))
print('5 Uppercase - ' + DigitToString(5, True))
print('13 Invalid (too large) - ' + DigitToString(19))
print('-4 Invalid (too small) - ' + DigitToString(-4))
print('A (not a number) - ' + DigitToString('A'))

print('\n\n\n Digitgroup to String Testing\n')
print('1 - ' + DigitgroupToString(1))
print('5 Uppercase - ' + DigitgroupToString(5, True))
print('13 - ' + DigitgroupToString(13))
print('40 - ' + DigitgroupToString(40))
print('82 - ' + DigitgroupToString(82))
print('100 - ' + DigitgroupToString(100))
print('513 - ' + DigitgroupToString(513))
print('781 - ' + DigitgroupToString(781))
print('1000 Invalid (too large) - ' + DigitgroupToString(1000))
print('-400 Invalid (too small) - ' + DigitgroupToString(-400))
print('A Invalid (NAN) - ' + DigitgroupToString("A"))
