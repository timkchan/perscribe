#Tim K. Chan
#14/02/17

import network	  # For Connecting to WIFI
from umqtt.simple import MQTTClient
import util

# Function to conenct to the wifi.
def wifiConnect(name, password):
	
	SSID = name
	PASSWORD = password

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

# Class of a publisher
class Publisher:

	# Class Constructor
	def __init__(self, server, clientId = 'clientId-UADVnHCKdM', defaultTopic = ''):
		self.server = server
		self.clientId = clientId
		self.defaultTopic = defaultTopic

	# Publish to server with message
	def publish(self, message = 'Testing', topic = None):
		tempTopic = topic or self.defaultTopic
		c = MQTTClient(self.clientId, self.server)
		c.connect()
		c.publish(tempTopic.encode('UTF-8'), message) 	#tempTopic.encode('UTF-8') ## b"esys/TBC/drugDealer"
		c.disconnect()

	# Repeatedly sending MQTT message to server ( for testing )
	def flush(self, msg = 'TESTING_TESTING_TESTING', times = 10):
		for _ in range(times):
			self.publish(msg)
			util.wait(300)

