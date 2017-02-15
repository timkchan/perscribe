from machine import Pin
import util

class Led:
	"""
	A simple class for controlling LEDs.

	Args:
		pin (machine.Pin): The pin where LED is connected.
	"""

	def __init__(self, pin_no):
		self.pin = Pin(pin_no, Pin.OUT)
		self.off()

	def on(self):
		self.pin.value(1)

	def off(self):
		self.pin.value(0)

	def blink(self, times = 5):
		for i in range(times):
			self.on()
			util.wait(300)
			self.off()
			util.wait(300)
