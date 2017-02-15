#Tim K. Chan
#14/02/17

import machine      # For Pins and i2C


import temp007
import vcnl4010
import led
import servo
import util         # Custom util functions

import jsonEncoder

import networkUtil  # Custom Network functions (WIFI + MQTT)
from umqtt.simple import MQTTClient


# Entry Point Indication
util.dots()

# Setup led
green = led.Led(13)
red = led.Led(15)

# Setup i2c Bus
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
util.msg('i2c bus created')

# Instantiate Temperature sensor
#Address of TMP007 Temperature Sensor
temp007Address = 64
tempSensor = temp007.Temp007(i2c, temp007Address)
util.msg('Temp007 instantiated, name: tempSensor')

# Instantiate Proximity sensor
#Address of VCNL4010 Proximity Sensor
proxAddress = 19
proxSensor = vcnl4010.Vcnl4010(i2c, proxAddress)
proxSensor.setup()
util.msg('Vcnl instantiated, name: proxSensor')

# Connecting to the Wifi
networkUtil.wifiConnect('EEERover', 'exhibition')

# Publisher for Embedded system class demo
esPub = networkUtil.Publisher('192.168.0.10', defaultTopic = 'esys/TBC/drugDealer')
util.msg('Publisher instantiated, name: esPub')





#Embedded Sys topic:                esys/TBC/drugDealer
#Embedded Sys MQTT broker IP:       192.168.0.10

#broker.hivemq.com