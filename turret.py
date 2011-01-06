#code by ITDaniher, written 2010-10-01 to 2010-10-25
#python API for TehTurret
#code licensed under a Beerware license. http://en.wikipedia.org/wiki/Beerware

import serial
import threading 
import struct
from time import sleep
import glob

#magic numbers from arduino sketch
tilt = 0x01
fire = 0x02
uv = 0x03
pan = 0x04
#magic numbers determining pan direction
right = 0b01
left = 0b10

class Turret:
	def __init__(self):
		try:
			self.ser = serial.Serial(glob.glob('/dev/ttyUSB*')[0], 9600, timeout=1)
		except serial.serialutil.SerialException:
			print "Your serial adapter could not be initialized for some reason. Exiting..."
		self.command = {'item':0, 'duration':0, 'newState':0, 'defState':0}
		self.states = {1:100,2:0,3:0,4:0}

	def send(self):
		"""Process command dictionary, pack data for uCU, send information via serial."""
		for k, v in self.command.items(): exec 'self.%s = %s' % (k, str(v))
		bytes = struct.pack('BBB', 0xFF, self.item, self.newState)
		self.ser.write(bytes)
		if self.duration != 0:
			sleep(self.duration)
			bytes = struct.pack('BBB', 0xFF, self.item, self.defState)
			self.ser.write(bytes)

	def do(self, item, newState, duration=0, defState=0):
		"""Generate command dictionary from arguments, thread an instance of 'send().'
		item - can be one of the magic numbers stored as 'tilt,' 'fire,' 'uv,' or 'pan.'
		newState - must be an integer or bool - describes the desired state of the item.
		duration - intended delay - nonblocking, as 'send()' is called as a thread. Defaults to 0.
		defState - default state - state 'item' reverts to after a delay of 'duration.'"""
		self.command = {'item':item, 'newState':newState, 'duration':duration, 'defState':defState}
		threading.Thread(target=self.send).start()
	
	def autoSync(self):
		"""provide a more lower-level interface to uCU than 'send'"""
		for k, v in self.states.items():
			print k, v
			bytes = struct.pack('BBB', 0xFF, k, int(v))
			self.ser.write(bytes)
		sleep(.005)
