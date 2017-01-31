import machine
import network
import time
from umqtt.simple import MQTTClient

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

# Function to print out objTemp at a certain time (ms) interval.
def objTempRoll(i):
	for __ in range(i):
		time.sleep_ms(300)
		print(objTemp())

# Function to conenct to the wifi.
def do_connect():
    
    SSID = 'MotoG3'
    PASSWORD = 'embedded'

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Network configuration:', sta_if.ifconfig())

do_connect()

def publish(message, server="broker.hivemq.com"):
    c = MQTTClient("clientId-UADVnHCKdM", server)
    c.connect()
    c.publish(b"practiceReminder", message)
    c.disconnect()

def publishTemp(i):
	for __ in range(i):
		time.sleep(3)
		publish(str(objTemp()))





