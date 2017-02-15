# Tim K. Chan
# 14/02/17

import util

class Vcnl4010:

	# Register of proximity measurement readings ( High byte (15:8) )
	proxHighByteReg = 0x87
	# Register of proximity measurement readings ( Low byte (7:0) )
	proxLowByteReg = 0x88
	# Register ByteSize
	regByteSize = 1

	# Class Constructor
	def __init__(self, i2c, i2cAddress):
		self.i2c = i2c
		self.i2cAddress = i2cAddress

	def setup(self, intensity = b'\x0D', proxMeasurementPerSec = b'\x01', ambientLightMeasurementPerSec = b'\x03'):
		self.i2c.writeto_mem(self.i2cAddress, 0x80, b'\x07')	# Set the mode to automatical measurment
		self.i2c.writeto_mem(self.i2cAddress, 0x82, proxMeasurementPerSec)
		self.i2c.writeto_mem(self.i2cAddress, 0x84, ambientLightMeasurementPerSec)

		self.i2c.writeto_mem(19, 0x83, intensity)

	# Reading proximity measurement
	def proximity(self):
		rawHighByte = self.i2c.readfrom_mem(self.i2cAddress, 0x87, 1)
		rawLowByte = self.i2c.readfrom_mem(self.i2cAddress, 0x88, 1)
		return rawHighByte[0] * 256 + rawLowByte[0]

	# Function to print out proximity at a certain time (ms) interval for i amount of times.
	def roll(self, ms = 300, times = 10):
		for __ in range(times):
			util.wait(ms)
			print(self.proximity())


# Reference:
# https://github.com/ControlEverythingCommunity/VCNL4010/blob/master/Python/VCNL4010.py