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


