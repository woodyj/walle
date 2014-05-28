class Eyes(object):
	def __init__(self):
		self.leftEyePin = 0
		self.rightEyePin = 0

	def setLeftEyeGPIO(self, pin):
		self.leftEyePin = pin

	def setRightEyeGPIO(self, pin):
		self.leftEyePin = pin

	def on(self, eye=both):
		if (eye == 'left'):
			print "Left eye on"
		elif (eye == 'right'):
			print "Right eye on"
		else:
			print "Both eyes on"

	def off(self, eye=both):
		if (eye == 'left'):
			print "Left eye off"
		elif (eye == 'right'):
			print "Right eye off"
		else:
			print "Both eyes off"

	def blink(self, eye=both):
		if (eye == 'left'):
			# left eye blink
		elif (eye == 'right'):
			# right eye blink
		else:
			# both eyes blink