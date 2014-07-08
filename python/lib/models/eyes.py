import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

class Eyes(object):
	def __init__(self, leftEyePin, rightEyePin):
		self.leftEyePin = leftEyePin
		GPIO.setup(self.leftEyePin, GPIO.OUT)

		self.rightEyePin = rightEyePin
		GPIO.setup(self.rightEyePin, GPIO.OUT)

	def testStr(self):
		return 'hello eyes'

	def on(self, eye='both'):
		if (eye == 'left'):
			print "Left eye on"
			GPIO.output(self.leftEyePin, 1)
		elif (eye == 'right'):
			print "Right eye on"
			GPIO.output(self.rightEyePin, 1)
		else:
			print "Both eyes on"
			GPIO.output(self.rightEyePin, 1)
			GPIO.output(self.leftEyePin, 1)

	def off(self, eye='both'):
		if (eye == 'left'):
			print "Left eye off"
			GPIO.output(self.leftEyePin, 0)
		elif (eye == 'right'):
			print "Right eye off"
			GPIO.output(self.rightEyePin, 0)
		else:
			print "Both eyes off"
			GPIO.output(self.rightEyePin, 0)
			GPIO.output(self.leftEyePin, 0)

	def blink(self, eye='both', delay=0.5, repeat=5):
		print("Eyes blink (%s)" % eye)
		self.off(eye)

		while(repeat > 0):
			self.on(eye)
			time.sleep(delay)
			self.off(eye)
			time.sleep(delay)
			repeat -= 1
			
