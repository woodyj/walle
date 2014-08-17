from eyes import Eyes

class Head(object):
	def __init__(self, servoController, servoPinPan, servoPinTilt, servoLimitPanMin, servoLimitPanMax, servoLimitTiltMin, servoLimitTiltMax):
		self.servoController = servoController
		self.servoPinPan = servoPinPan
		self.servoPinTilt = servoPinTilt
		self.servoLimitPanMax = servoLimitPanMax
		self.servoLimitPanMin = servoLimitPanMin
		self.servoLimitTiltMin = servoLimitTiltMin
		self.servoLimitTiltMax = servoLimitTiltMax
		self.panPosition = None
		self.tiltPosition = None
		#self.eyes = new Eyes()

	#def turnCenter(self):

	#def turnLeft(self):

	#def turnRight(self):

	def pan(self, servoPosition):
		if (servoPosition > self.servoLimitPanMax):
			servoPosition = self.servoLimitPanMax

		if (servoPosition < self.servoLimitPanMin):
			servoPosition = self.servoLimitPanMin

		self.servoController.setPWM(self.servoPinPan, 0, servoPosition)
		self.panPosition = servoPosition

	def tilt(self, servoPosition):
		if (servoPosition > self.servoLimitTiltMax):
			servoPosition = self.servoLimitTiltMax

		if (servoPosition < self.servoLimitTiltMin):
			servoPosition = self.servoLimitTiltMin

		self.servoController.setPWM(self.servoPinTilt, 0, servoPosition)
		self.tiltPosition = servoPosition

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