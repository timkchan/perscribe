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

	def setUp():
		self.i2c.writeto_mem(self.i2cAddress, 0x80, b'\x07')
		self.i2c.writeto_mem(self.i2cAddress, 0x82, b'\x01')
		self.i2c.writeto_mem(self.i2cAddress, 0x84, b'\x03')

	# Reading proximity measurement
	def prox(self):
		rawHighByte = self.i2c.readfrom_mem(self.i2cAddress, Vcnl4010.proxHighByteReg, Vcnl4010.regByteSize)
		rawLowByte = self.i2c.readfrom_mem(self.i2cAddress, Vcnl4010.proxLowByteReg, Vcnl4010.regByteSize)
		return [rawLowByte, rawHighByte]



	# VCNL4010 address, 0x13(19)
	# Read data back from 0x85(133), 4 bytes
	# luminance MSB, luminance LSB, Proximity MSB, Proximity LSB
	data = bus.read_i2c_block_data(0x13, 0x85, 4)

	# Convert the data
	luminance = data[0] * 256 + data[1]
	proximity = data[2] * 256 + data[3]




	# Function to print out objTemp at a certain time (ms) interval for i amount of times.
	def objTempRoll(self, ms, times):
		for __ in range(times):
			time.sleep_ms(ms)
			print(self.objTemp())

