**Embedded System Project - IC 2017**

This is the software for the first prototype of a pill dispenser platform. This unit will assist patients in taking medicine to enable them to be more independent and have a higher quality of life.

This system is designed on the micropython platform. To learn more click [here!](www.micropython.org)

![Image of Pill](https://cdn.pixabay.com/photo/2015/10/01/00/50/pills-dispenser-966334_960_720.png)

Please see below for the block diagram of the system.

![BlkDiag](https://raw.githubusercontent.com/timkchan/practiceReminder/master/README_Material/BLKDiag.png)

The componants used:
Feather HUZZAH ESP8266
Adafruit TMP007 Sensor Breakout

Software needed:

	To get Esptool: pip
		upgrade pip:
			`pip install --upgrade pip`

	To flash Feather board: Esptool
		Getting esptool.py:
			`pip install esptool`

	To connect mac with Feather board with COM port: Screen [built-in in mac]
	MicroPython for ESP 8266
		http://micropython.org/download#esp8266

Find which port is Feather connected to
	ls /dev/cu.*
	e.g. /dev/cu.SLAB_USBtoUART

Installing MicroPython
	- Erase old firmware
		`esptool.py --port /dev/cu.SLAB_USBtoUART erase_flash`
	- Flash Firmware
		`esptool.py --port /dev/cu.SLAB_USBtoUART --baud 115200 write_flash --flash_size=detect 0 ~/DEV/EmbeddedSystem/firmware/esp8266-20170108-v1.8.7.bin`

Connect to Feather board via COM prot:
	- Establish connection
		`screen /dev/cu.SLAB_USBtoUART 115200`
		(You might need to press `return` key several times to get >>> to appear)

I2C Setup
	-initialize access to the I2C bus
		`import machine`
		`i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))`
	- Scan for connected i2c device
		`i2c.scan()`
			e.g. [64]

TMP007 Pin setup
	AD1 AD2 are customised address e.g. AD1=AD2=GROUND
		=> SMBus Address = 1000000 First 5 bits are set by manufacturer.
		=> the last bit (LSB) made up the byte indicates read (1) or write (0)


The system uses HiveMQ as the MQTT broker - you can view it's status [here!](http://www.mqtt-dashboard.com/)
