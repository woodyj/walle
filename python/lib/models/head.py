from eyes import Eyes

class Head(object):
	def __init__(self):
		self.turnServo = []
		self.lookServo = []
		self.eyes = new Eyes()

	#def turnCenter(self):

	#def turnLeft(self):

	#def turnRight(self):

	def leftEyeBlink(self):
		self.eyes.blink(eye='left')

	def leftEyeOn(self):
		self.eyes.on(eye='left')

	def leftEyeOff(self):
		self.eyes.off(eye='left')

	def rightEyeBlink(self):
		self.eyes.blink(eye='right')

	def rightEyeOn(self):
		self.eyes.on(eye='right')

	def rightEyeOff(self):
		self.eyes.off(eye='right')

	def bothEyesOn(self):
		self.leftEyeOn()
		self.rightEyeOn()

	def bothEyesOff(self):
		self.leftEyeOff()
		self.rightEyeOff()