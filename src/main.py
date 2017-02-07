import machine
import network
import time
import temp007_Tim
import led_Tim
import servo
from umqtt.simple import MQTTClient

print('main.py loading...')
for __ in range(10):
	time.sleep_ms(300)
	print('.')

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
print('i2c bus created')

#Address of TMP007
address = 64

sensor = temp007.Temp007(i2c, address)
print('Temp007 instance created')

print('Try dieTemp() or objTemp()')



# Function to conenct to the wifi.
def do_connect():
    
    SSID = 'EEERover'
    PASSWORD = 'exhibition'

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

#do_connect()

#broker.hivemq.com

def publish(message, server="192.168.0.10"):
    c = MQTTClient("clientId-UADVnHCKdM", server)
    c.connect()
    c.publish(b"esys/forgotton/practiceReminder", message)
    c.disconnect()

def publishTemp(i):
	for __ in range(i):
		time.sleep_ms(300)
		t = str(sensor.objTemp())
		print(t)
		publish(t)





