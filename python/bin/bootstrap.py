import _config_
import sys, time, tty, termios

from models.drivers.pwm.Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(_config_.pwmI2CAddr, debug=_config_.pwmI2CDebug)
pwm.setPWMFreq(_config_.pwmFreq)

from models.head import Head

head = Head(servoController=pwm, servoPinPan=_config_.servoPinHeadPan, servoPinTilt=_config_.servoPinHeadTilt, servoLimitPanMin=_config_.servoLimitHeadRight, servoLimitPanMax=_config_.servoLimitHeadLeft, servoLimitTiltMin=_config_.servoLimitHeadDown, servoLimitTiltMax=_config_.servoLimitHeadUp)
head.pan(_config_.servoLimitHeadCenter)
head.tilt(_config_.servoLimitHeadLevel)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

"""
i = head.servoLimitPanMin

while (i < head.servoLimitPanMax):
	i += 1
	head.pan(i)
	time.sleep(0.005)

head.pan(_config_.servoLimitHeadCenter)
#time.wait(0.1)
"""
import sys, tty, termios, time

stop = False

while (not stop):
    char = getch()

    if (char == 'q'):
    	print "Quitting..."
    	stop = True

    if (char == 'j' or char == 'u' or char == 'n'):
    	head.pan(head.panPosition+5)

    if (char == 'l' or char == 'o' or char == ','):
    	head.pan(head.panPosition-5)

    if (char == 'i' or char == 'u' or char == 'o'):
    	head.tilt(head.tiltPosition+5)

    if (char == 'm' or char == 'n' or char == ','):
    	head.tilt(head.tiltPosition-5)

    if (char == 'k'):
    	head.pan(_config_.servoLimitHeadCenter)
    	head.tilt(_config_.servoLimitHeadLevel)