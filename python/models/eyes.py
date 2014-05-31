class Eyes(object):
	def __init__(self, leftEyePin, rightEyePin):
		self.leftEyePin = leftEyePin
		self.rightEyePin = rightEyePin

	def testStr(self):
		return 'hello eyes'

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