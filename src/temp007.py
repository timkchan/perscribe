class Temp007:

	# Register of die temp. sensor
	dieReg = 1
	# Register of obj temp. sensor
	objReg = 3
	# Register Byte Size
	regByteSize = 2

	# Class Constructor
	def __init__(self, i2c, i2cAddress):
		self.i2c = i2c
		self.i2cAddress = i2cAddress

	# Reading tmeperature on die
	def dieTemp(self):
		rawByte = self.i2c.readfrom_mem(self.i2cAddress, Temp007.dieReg, Temp007.regByteSize)
		return (rawByte[0]*32+rawByte[1])*0.03125

	# Reading temperature of object
	def objTemp(self):
		rawByte = self.i2c.readfrom_mem(self.i2cAddress, Temp007.objReg, Temp007.regByteSize)
		return (rawByte[0]*32+rawByte[1])*0.03125

	# Function to print out objTemp at a certain time (ms) interval for i amount of times.
	def objTempRoll(self, ms, times):
		for __ in range(times):
			time.sleep_ms(ms)
			print(self.objTemp())