# Tail.py
#
# Implementation of the "Tail -f" function of Linux






# User specifies which file to follow

# System copies file for reading as filename.tailbase
# System reads last 5 lines of tailbase
# System returns last 5lines of tailbase
# System stores the read position of the last character - STO1

# LOOP - System checks file size of tailbase and original file

# IF - Change in file size
	# Open orig file for reading
	# Scan to position stored - STO1
	# Read file to end
	# Append that to Tailbase
# ENDIF
