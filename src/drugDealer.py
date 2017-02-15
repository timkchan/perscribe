# Tim K. Chan
# 15/02/17

import time 
import util

# Schedule is the a list of time tuple, timeDelta is the time allowed to take the pill before or after the schedule in second
class DrugDealer:

	def __init__(self, schedule, timeDelta = 5):
		self.schedule = schedule
		self.timeDelta = timeDelta

	def run(self):
		for i in range(len(self.schedule)):
			while True:
				if util.timeBetween(time.localtime(), self.schedule[i], self.timeDelta):
					green.on()
					util.wait(1000)
					break