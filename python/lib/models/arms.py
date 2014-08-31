class Arms(object):
	def __init__(self, servoController, servoPinLeft, servoPinRight, servoLimitMin, servoLimitMax):
		self.servoController = servoController
		self.servoPinLeft = servoPinLeft
		self.servoPinRight = servoPinRight
		self.servoLimitMin = servoLimitMin
		self.servoLimitMax = servoLimitMax
		self.leftPosition = None
		self.rightPosition = None
		self.centerPosition = int(servoLimitMax - ((servoLimitMax - servoLimitMin) / 2))
		self.centerBoth()

	def moveLeft(self, servoPosition):
		if (servoPosition > self.servoLimitMax):
			servoPosition = self.servoLimitMax

		if (servoPosition < self.servoLimitMin):
			servoPosition = self.servoLimitMin

		self.servoController.setPWM(self.servoPinLeft, 0, servoPosition)
		self.leftPosition = servoPosition

	def upLeft(self, distance):
		servoPosition = self.leftPosition - distance

		if (servoPosition < self.servoLimitMin):
			servoPosition = self.servoLimitMin

		self.servoController.setPWM(self.servoPinLeft, 0, servoPosition)
		self.leftPosition = servoPosition

	def downLeft(self, distance):
		servoPosition = self.leftPosition + distance

		if (servoPosition > self.servoLimitMax):
			servoPosition = self.servoLimitMax

		self.servoController.setPWM(self.servoPinLeft, 0, servoPosition)
		self.leftPosition = servoPosition

	def moveRight(self, servoPosition):
		if (servoPosition > self.servoLimitMax):
			servoPosition = self.servoLimitMax

		if (servoPosition < self.servoLimitMin):
			servoPosition = self.servoLimitMin

		self.servoController.setPWM(self.servoPinRight, 0, servoPosition)
		self.rightPosition = servoPosition

	def upRight(self, distance):
		servoPosition = self.rightPosition + distance

		if (servoPosition > self.servoLimitMax):
			servoPosition = self.servoLimitMax

		self.servoController.setPWM(self.servoPinRight, 0, servoPosition)
		self.rightPosition = servoPosition

	def downRight(self, distance):
		servoPosition = self.rightPosition - distance

		if (servoPosition < self.servoLimitMin):
			servoPosition = self.servoLimitMin

		self.servoController.setPWM(self.servoPinRight, 0, servoPosition)
		self.rightPosition = servoPosition

	def getCenterServoPosition(self):
		return self.centerPosition

	def centerLeft(self):
		self.servoController.setPWM(self.servoPinLeft, 0, self.getCenterServoPosition())
		self.leftPosition = self.getCenterServoPosition()

	def centerRight(self):
		self.servoController.setPWM(self.servoPinRight, 0, self.getCenterServoPosition())
		self.rightPosition = self.getCenterServoPosition()

	def centerBoth(self):
		self.centerLeft()
		self.centerRight()