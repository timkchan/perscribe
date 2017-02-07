import paho.mqtt.client as mqtt
import time 

instrument_status = False #This variable indicates if the instrument is currently in use
last_update = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("practiceReminder/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message Recieved: " + msg.topic+" "+float(msg.payload))

def check_times():
	print "Blah"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

print time.time()
run = True
while run == True:
	client.loop()
	
	


