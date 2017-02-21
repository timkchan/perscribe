#Tim K. Chan
#14/02/17

import machine      # For Pins and i2C
import utime

import temp007
import vcnl4010
import led
import servo
import util         # Custom util functions
import servoController

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

# Instantiate 2 servos
top = servo.Servo(machine.Pin(12), 50, 350, 2400, 180)
bottom = servo.Servo(machine.Pin(0), 50, 350, 2400, 180)
util.msg('2 servos instantiated, name: top; bottom')

# Instantiate servo controller
servoCtrl = servoController.ServoController(top, bottom)
util.msg('Servos controller instantiated, name: servoCtrl')

# Connecting to the Wifi
# networkUtil.wifiConnect('EEERover', 'exhibition')


# #Grab the time from the MQTT broker and set the RTC
# timeSet = networkUtil.Publisher('192.168.0.10', defaultTopic = 'esys/time')
# timeSet.subscribe()

# Publisher for Embedded system class demo
# esPub = networkUtil.Publisher('broker.hivemq.com', defaultTopic = 'esys/TBC/drugDealer')
# util.msg('Publisher instantiated, name: esPub')

##########################################################################################
##########################################################################################
### DEMO

# Make a scheduel for demo:
currentTime = list(utime.localtime())
schedule = []
doseInterval = 10

for i in range(100):
    temp = list(currentTime)
    temp[5] = temp[5] + doseInterval * (i+1)
    schedule.append(tuple(temp))

# Running the pill dispenser
taken = False
for i in range(len(schedule)):
    while True:
        # Time to go to next dose time
        if (utime.mktime(utime.localtime()) > utime.mktime(schedule[i])):
            if taken == False:
                msgDict = {'time': utime.localtime(), 'id': 101, 'taken': False, 'temp': tempSensor.objTemp()}
                msg = jsonEncoder.pack(msgDict)
                # esPub.publish(msg)
                print('Pill Missed!', msg)
                servoCtrl.next()
            
            break
        # Still within dosage time, checking
        if util.timeBetween(utime.localtime(), schedule[i], 3):
            print('ttt')
            green.on()
            red.off()
            if proxSensor.proximity() > 2100:
                msgDict = {'time': utime.localtime(), 'id': 101, 'taken': True, 'temp': tempSensor.objTemp()}
                msg = jsonEncoder.pack(msgDict)
                # esPub.publish(msg)
                print('Pill Taken!', msg)
                taken == True
                servoCtrl.next()
                break
        else:
            print('nttt')
            green.off()
            red.on()
        util.wait(100)








#Embedded Sys topic:                esys/TBC/drugDealer
#Embedded Sys MQTT broker IP:       192.168.0.10

#broker.hivemq.com
