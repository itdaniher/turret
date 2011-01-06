#code by ITDaniher, written 2010-10-01 to 2010-10-14              
#superfly pure-python joystick driver for use on Linux 
#created for use with TehTurret.
#code licensed under a Beerware license. http://en.wikipedia.org/wiki/Beerware

import struct
import glob
import threading
from time import sleep

class Joystick:

	def __init__(self):
		self.newButtonInfo = threading.Event()
		self.newAxisInfo = threading.Event()
		self.js = open(glob.glob('/dev/input/js*')[0], 'r')
		self.button = {}
		self.axis = {}
		#[("time", c_uint32), ("value", c_int16), ("type", c_uint8), ("number", c_uint8)]
		self.format = 'LhBB'

	def monitor(self):
		"""Monitors /dev/input/js* device and records information in the dictionaries
		self.button and self.axis.
		Also triggers the events newAxisInfo and newButtonInfo"""
		while True:
			JS_EVENT_BUTTON = 0x01#button pressed/released
			JS_EVENT_AXIS = 0x02#joystick moved
			JS_EVENT_INIT = 0x80#initial state of device
			#read bytes from the js device and unpack it according to the format above
			self.info = struct.unpack(self.format, self.js.read(struct.calcsize(self.format)))
			time = self.info[0]
			value = self.info[1]
			type = self.info[2] & ~JS_EVENT_INIT
			number = self.info[3]
			if type == JS_EVENT_BUTTON:
				self.button[number] = value
				self.newButtonInfo.set()
			elif type == JS_EVENT_AXIS:
				self.axis[number] = value/32767.0
				self.newAxisInfo.set()

if __name__ == '__main__':
	js = Joystick()
	jsThread = threading.Thread(target=js.monitor)
	jsThread.daemon = True
	jsThread.start()
	while True:
		if js.newButtonInfo.isSet():
			print js.button
			js.newButtonInfo.clear()
