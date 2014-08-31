import _config_
#import sys, time, tty, termios
import time

import termios, fcntl, sys, os
fd = sys.stdin.fileno()

from models.drivers.pwm.Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(_config_.pwmI2CAddr, debug=_config_.pwmI2CDebug)
pwm.setPWMFreq(_config_.pwmFreq)

from models.head import Head
from models.arms import Arms
from models.voice import Voice

head = Head(
    servoController=pwm,
    servoPinPan=_config_.servoPinHeadPan,
    servoPinTilt=_config_.servoPinHeadTilt,
    servoLimitPanMin=_config_.servoLimitHeadRight,
    servoLimitPanMax=_config_.servoLimitHeadLeft,
    servoLimitTiltMin=_config_.servoLimitHeadDown,
    servoLimitTiltMax=_config_.servoLimitHeadUp
)
head.pan(_config_.servoLimitHeadCenter)
head.tilt(_config_.servoLimitHeadLevel)

arms = Arms(
    servoController=pwm,
    servoPinLeft=_config_.servoPinArmLeft,
    servoPinRight=_config_.servoPinArmRight,
    servoLimitMin=_config_.servoLimitArmMin,
    servoLimitMax=_config_.servoLimitArmMax
)

voice = Voice(volume=_config_.voiceDefaultVolume)

"""
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
oldterm = ''
oldflags = []

def getKeyPress():
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:
        return sys.stdin.read(1)
    except IOError:
        pass

"""
i = head.servoLimitPanMin

while (i < head.servoLimitPanMax):
    i += 1
    head.pan(i)
    time.sleep(0.005)

head.pan(_config_.servoLimitHeadCenter)
#time.wait(0.1)
"""

try:
    minServoSpeed = 1
    maxServoSpeed = 30
    servoSpeed = 10
    stop = False

    while (not stop):
        char = getKeyPress()

        if (char == 'q'):
            print "Quitting..."
            stop = True

        if (char == '='):
            servoSpeed += 2
            if (servoSpeed > maxServoSpeed):
                servoSpeed = maxServoSpeed

        if (char == '-'):
            servoSpeed -= 2
            if (servoSpeed < minServoSpeed):
                servoSpeed = minServoSpeed

        if (char == 'j' or char == 'u' or char == 'n'):
            head.pan(head.panPosition + servoSpeed)

        if (char == 'l' or char == 'o' or char == ','):
            head.pan(head.panPosition - servoSpeed)

        if (char == 'i' or char == 'u' or char == 'o'):
            head.tilt(head.tiltPosition + servoSpeed)

        if (char == 'm' or char == 'n' or char == ','):
            head.tilt(head.tiltPosition - servoSpeed)

        if (char == 'k'):
            head.pan(_config_.servoLimitHeadCenter)
            head.tilt(_config_.servoLimitHeadLevel)

        if (char == 'w'):
            arms.upLeft(servoSpeed)

        if (char == 's'):
            arms.centerLeft()

        if (char == 'x'):
            arms.downLeft(servoSpeed)

        if (char == 'e'):
            arms.upLeft(servoSpeed)
            arms.upRight(servoSpeed)

        if (char == 'd'):
            arms.centerBoth()

        if (char == 'c'):
            arms.downLeft(servoSpeed)
            arms.downRight(servoSpeed)

        if (char == 'r'):
            arms.upRight(servoSpeed)

        if (char == 'f'):
            arms.centerRight()

        if (char == 'v'):
            arms.downRight(servoSpeed)

        if (char == '1'):
            voice.say('walle_1')

        if (char == '2'):
            voice.say('walle_2')

        if (char == '3'):
            voice.say('walle_3')

        if (char == '4'):
            voice.say('eva_2')

        if (char == '5'):
            voice.say('tada')

        if (char == '6'):
            voice.say('whoa')

        if (char == '7'):
            voice.say('grunting')

        if (char == '8'):
            voice.say('buynlarge')

        if (char == '9'):
            voice.sing('background_music')

        if (char == '0'):
            voice.sing('la vie en rose')


finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)