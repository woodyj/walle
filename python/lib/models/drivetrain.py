#from servo import Servo

class Drivetrain(object):
	def __init__(self, servoController, servoPinLeft, servoPinRight, servoLimitCW, servoLimitCCW):
		self.servoController = servoController
		self.servoPinLeft = servoPinLeft
		self.servoPinRight = servoPinRight
		self.servoLimitCW = servoLimitCW
		self.servoLimitCCW = servoLimitCCW

	def forward(self):
		self.servoController.setPWM(self.servoPinLeft, 0, self.servoLimitCCW)
		self.servoController.setPWM(self.servoPinRight, 0, self.servoLimitCW)

	def backward(self):
		self.servoController.setPWM(self.servoPinLeft, 0, self.servoLimitCW)
		self.servoController.setPWM(self.servoPinRight, 0, self.servoLimitCCW)

	def stop(self):
		self.servoController.setPWM(self.servoPinLeft, 0, 0)
		self.servoController.setPWM(self.servoPinRight, 0, 0)

	def spinLeft(self):
		self.servoController.setPWM(self.servoPinLeft, 0, self.servoLimitCCW)
		self.servoController.setPWM(self.servoPinRight, 0, self.servoLimitCCW)

	def spinRight(self):
		self.servoController.setPWM(self.servoPinLeft, 0, self.servoLimitCW)
		self.servoController.setPWM(self.servoPinRight, 0, self.servoLimitCW)