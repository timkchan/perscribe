#Tim K. Chan
#14/02/17

import time

patience = 700			# Default waiting time for displays

# Pause for certain ms (for print out redability)
def wait(ms = patience):
	time.sleep_ms(ms)

# Print dots that last for certain ms (for print out redability)
def dots(ms = patience):
	print('main.py loading...')
	for __ in range(ms/100):
		wait(100)
		print('.', end = '')
	print()

# Print out message
def msg(msg):
	print('Feather: ' + msg)
	wait()

# Compare 2 time from utime.localtime(), return +1 if A is after B, 0 if A == B, -1 if A is before B
def timeCompareS(timeA, timeB):
	timeAs = time.mktime(timeA)
	timeBs = time.mktime(timeB)
	
	if timeAs > timeBs:
		return 1
	if timeAs < timeBs:
		return -1
	return 0

# Compare a time A is between time B +- Delta second
def timeBetween(timeA, timeB, delta):
	timeAs = time.mktime(timeA)
	timeBs = time.mktime(timeB)
	timeUpper = timeBs + delta
	timeLower = timeBs - delta
	return timeAs >= timeLower and timeAs <= timeUpper


