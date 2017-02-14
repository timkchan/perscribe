class Vcnl4010:

	# Register of proximity measurement readings ( High byte (15:8) )
	proxHighByteReg = 7
	# Register of proximity measurement readings ( Low byte (7:0) )
	proxLowByteReg = 8
	# Register ByteSize
	regByteSize = 1

	# Class Constructor
	def __init__(self, i2c, i2cAddress):
		self.i2c = i2c
		self.i2cAddress = i2cAddress

	# Reading proximity measurement
	def value(self):
		rawHighByte = self.i2c.readfrom_mem(self.i2cAddress, Vcnl4010.proxHighByteReg, Vcnl4010.regByteSize)
		rawLowByte = self.i2c.readfrom_mem(self.i2cAddress, Vcnl4010.proxLowByteReg, Vcnl4010.regByteSize)
		return [rawLowByte, rawHighByte]



	# Function to print out objTemp at a certain time (ms) interval for i amount of times.
	def objTempRoll(self, ms, times):
		for __ in range(times):
			time.sleep_ms(ms)
			print(self.objTemp())
