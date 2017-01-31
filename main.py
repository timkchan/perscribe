import machine
import time

print('main.py loading...')

for __ in range(10):
	time.sleep_ms(300)
	print('.')

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
print('i2c bus created')

#Address of TMP007
address = 64
#Register of die temp. sensor
dieReg = 1
#Register of obj temp. sensor
objReg = 3

def dieTemp():
	rawByte = i2c.readfrom_mem(address, dieReg, 2)
	return (rawByte[0]*32+rawByte[1])*0.03125

def objTemp():
	rawByte = i2c.readfrom_mem(address, objReg, 2)
	return (rawByte[0]*32+rawByte[1])*0.03125

print('main.py loaded successfully')
print('hint:')
print('Try dieTemp() or objTemp()')

def objTempRoll(i):
	for __ in range(i):
		time.sleep_ms(300)
		print(objTemp())