import _config_
import time
import cwiid
import sys
import os
import termios
import fcntl
fd = sys.stdin.fileno()

from models.drivers.pwm.Adafruit_PWM_Servo_Driver import PWM
pwm = PWM(_config_.pwmI2CAddr, debug=_config_.pwmI2CDebug)
pwm.setPWMFreq(_config_.pwmFreq)

from models.head import Head
from models.arms import Arms
from models.voice import Voice
from models.drivetrain import Drivetrain

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

tracks = Drivetrain(
    servoController=pwm,
    servoPinLeft=_config_.servoPinTrackLeft,
    servoPinRight=_config_.servoPinTrackRight,
    servoLimitCW=_config_.servoLimitTrackCW,
    servoLimitCCW=_config_.servoLimitTrackCCW
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

minServoSpeed = 1
maxServoSpeed = 30
servoSpeed = 10
stop = False
wiiRemote = None

def displayScreen(mode):
    if (mode == 'wii-connect'):
        os.system('clear')
        print 'Press 1 & 2 on wii remote to connect...'

    elif (mode == 'wii-connect-failed'):
        os.system('clear')
        print 'Failed to connect to Wii remote.  Switching to keyboard mode...'

    elif (mode == 'wii-disconnect'):
        os.system('clear')
        print 'Disconnecting Wii remote...'

    elif (mode == 'main'):
        os.system('clear')
        print 'WALL-E Control (keyboard mode)'
        print '=============================='
        print ''
        print 'Keyboard Controls'
        print '--------------------------'
        print ''
        print 'Increase servo speed: ='
        print 'Decrease servo speed: -'
        print ''
        print 'Left arm up: w'
        print 'Left arm out: s'
        print 'Left arm down: x'
        print ''
        print 'Right arm up: r'
        print 'Right arm out: f'
        print 'Right arm up: v'
        print ''
        print 'Head tilt up: i'
        print 'Head tilt down: m'
        print 'Head center: k'
        print 'Head pan left: j'
        print 'Head pan right: l'
        print ''
        print 'QUIT: q'
        print ''

        if (wiiRemote):
            print 'Wii Remote Controls'
            print '--------------------------'
            print ''
            print 'Button A: '
            print 'Button B: '
            print 'Button 1: '
            print 'Button 2: '
            print 'Button (-): '
            print 'Button (+): '
            print 'D-pad: tracks'
            print 'Home button: enter keyboard mode'
        else:
            print 'Connect Wii remote: ]'
            print ''


displayScreen('main')

#try:

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

    if (char == ']'):
        displayScreen('wii-connect')
        wiiRemote = None 
        i = 2 
        while not wiiRemote: 
          try: 
            wiiRemote = cwiid.Wiimote() 
            wiiRemote.rumble = True
            time.sleep(0.3)
            wiiRemote.rumble = False
            displayScreen('main')
          except RuntimeError: 
            if (i > 10):
                displayScreen('wii-connect-failed')
                time.sleep(1)
                break 
            print "Error opening wiimote connection" 
            print "attempt " + str(i) 
            i += 1 

        #set Wiimote to report button presses and accelerometer state 
        wiiRemote.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC 
         
        #turn on led to show connected 
        wiiRemote.led = 1

        """
        while wiiRemote:
            print ''
            print '---------------------------------------------------------------'
            print wiiRemote.state
            print wiiRemote.state['buttons']
            print wiiRemote.state['acc']
            time.sleep(0.5)
        """

    #while (wiiRemote):
    if (wiiRemote):
        wiiBut = wiiRemote.state['buttons']
        wiiAcc = wiiRemote.state['acc']

        move = False

        if (wiiBut & 128):
            wiiRemote = False
            displayScreen('wii-disconnect')
            time.sleep(1)
            displayScreen('main')

        if (wiiBut & 2):
            voice.say('whoa')

        if (wiiBut & 1):
            voice.say('tada')

        if (wiiBut & 256):
            move = True
            tracks.spinLeft()

        if (wiiBut & 512):
            move = True
            tracks.spinRight()

        if (wiiBut & 1024):
            move = True
            tracks.backward()

        if (wiiBut & 2048):
            move = True
            tracks.forward()

        if (not move):
            tracks.stop()

        #os.system('clear')
        #print ('Buttons: %s' % wiiBut)
        #print 'Acc:'
        #print wiiAcc

"""
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
"""