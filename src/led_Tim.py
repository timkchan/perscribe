from machine import Pin

class Led:
	"""
	A simple class for controlling LEDs.

	Args:
		pin (machine.Pin): The pin where LED is connected.
	"""

	def __init__(self, pin_no):
		self.pin = Pin(pin_no, Pin.OUT)

	def on(self):
		self.pin.value(1)

	def off(self):
		self.pin.value(0)