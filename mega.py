#code by ITDaniher, written 2010-10-01 to 2010-10-25
#manual runtime code for TehTurret - allows soft realtime control via xbox360 controller.
#code licensed under a Beerware license. http://en.wikipedia.org/wiki/Beerware

import turret
import joystick
import threading
import xbox360
from time import sleep

#keyword definitions for turret commands
i = 'item'
d = 'duration'
nS = 'newState'
dS = 'defState'

speedSwap = 0
speedMultiplier = 1.0

t = turret.Turret()

js = joystick.Joystick()
jsThread = threading.Thread(target=js.monitor)
jsThread.daemon = True
jsThread.start()

threshold = .25

while True:
	if js.newButtonInfo.isSet():
		for button, value in js.button.items():
			if button == xbox360.buttonB and value == 1:
				quit()
			elif button == xbox360.buttonX:
				t.states[turret.uv] = value
			elif button == xbox360.buttonY:
				t.states[turret.tilt] = 100
			elif button == xbox360.buttonRStick and value == 1:
				speedSwap ^= 1
				if speedSwap == 0:
					speedMultiplier = 1.0
				else:
					speedMultiplier = .25
		t.autoSync()
		js.newButtonInfo.clear()
	if js.newAxisInfo.isSet():
		for axis, value in js.axis.items():
			if axis == xbox360.rThumbPan:
				if value > threshold:
					t.states[turret.pan] = turret.left
				elif value < -threshold:
					t.states[turret.pan] = turret.right
				else:
					t.states[turret.pan] = 0
			elif axis == xbox360.rThumbTilt:
				if value > threshold or value < -threshold:
					t.states[turret.tilt] += value*speedMultiplier
				else:
					js.newAxisInfo.clear()
			elif axis == xbox360.rTrigger:
					if value > 0:
						t.states[turret.fire]=1
					elif value < 0:
						t.states[turret.fire]=0
		t.autoSync()
