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
		self.mqttClient = MQTTClient(clientId, server)
		self.defaultTopic = defaultTopic

	# Publish to server with message
	def publish(self, message = 'Testing', topic = None):
		tempTopic = topic or self.defaultTopic
		self.mqttClient.connect()
		self.mqttClient.publish(tempTopic.encode('UTF-8'), message) 	#tempTopic.encode('UTF-8') ## b"esys/TBC/drugDealer"
		self.mqttClient.disconnect()

	# Subscribe from publisher
	def subscribe(self, topic = None, callBack = ( lambda topic, msg: print((topic, msg)) )):
		tempTopic = topic or self.defaultTopic
		self.mqttClient.connect()
		self.mqttClient.subscribe(tempTopic.encode('UTF-8'))
		while True:
			if True:
				# Blocking wait for message
				self.mqttClient.wait_msg()
			else:
				# Non-blocking wait for message
				self.mqttClient.check_msg()
				# Then need to sleep to avoid 100% CPU usage (in a real
				# app other useful actions would be performed instead)
				time.sleep(1)
		mqttClient.disconnect()



	# Repeatedly sending MQTT message to server ( for testing )
	def flush(self, msg = 'TESTING_TESTING_TESTING', times = 10):
		for _ in range(times):
			self.publish(msg)
			util.wait(300)

