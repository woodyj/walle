import _config_
#from models.eyes import Eyes
from models.eyes import Eyes
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

eyes = Eyes(leftEyePin=17, rightEyePin=18)
print eyes.testStr()

eyes.on('left')
time.sleep(1)
eyes.off('left')

eyes.on('right')
time.sleep(1)
eyes.off('right')

eyes.blink('both')
time.sleep(5)
eyes.off('both')

print 'clean up'
GPIO.cleanup()
