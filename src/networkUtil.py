#Tim K. Chan
#14/02/17

import network	  # For Connecting to WIFI
from umqtt.simple import MQTTClient
import util

import machine

import ujson

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

def setTime(topic, time_raw):
	print(time_raw)
	tmp = ujson.dumps(time_raw)
	print(tmp)
	tmp = tmp[13:-4]
	#tmp = tmp.split(": -")
	print(tmp)
	print(int(tmp[0:4]), int(tmp[5:7]), int(tmp[8:10]), int(tmp[11:13]), int(tmp[14:16]), int(tmp[17:19]), 0, 0)
	machine.RTC().datetime((int(tmp[0:4]), int(tmp[5:7]), int(tmp[8:10]), int(tmp[11:13]), int(tmp[14:16]), int(tmp[17:19]), 0, 0))

	

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
	#def subscribe(self, topic = None, callBack = ( lambda topic, msg: print((topic, msg)) )):
	def subscribe(self, topic = None, callBack = setTime):
		tempTopic = topic or self.defaultTopic
		self.mqttClient.set_callback(callBack)
		self.mqttClient.connect()
		self.mqttClient.subscribe(tempTopic.encode('UTF-8'))
		global acquired
		acquired = False
		print('Waiting for timing packet...')
		for i in range(0, 21):
			# Blocking wait for message
			self.mqttClient.check_msg()
			util.wait(5000)
			print('.')
		self.mqttClient.disconnect()

	# Repeatedly sending MQTT message to server ( for testing )
	def flush(self, msg = 'TESTING_TESTING_TESTING', times = 10):
		for _ in range(times):
			self.publish(msg)
			util.wait(300)

