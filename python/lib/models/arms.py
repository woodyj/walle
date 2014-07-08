#from servo import Servo

class Arms(object):
	def __init__(self):
		self.leftArmServo = new Servo()
		self.rightArmServo = new Servo()

	def setPosition(self, arm, modulation):
		if (arm == 'left'):
			self.leftArmServo.setPosition(modulation)
		else:
			self.rightArmServo.setPosition(modulation)

	def getPosition(self, arm):
		if (arm == 'left'):
			return self.leftArmServo.getPosition()
		else:
			return self.rightArmServo.getPosition()