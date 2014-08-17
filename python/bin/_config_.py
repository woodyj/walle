import os
import sys
libraryPath = str(os.path.dirname(os.path.realpath(__file__)) + '/../lib')
sys.path.insert(1, libraryPath)

# ------- Servo Driver Settings ------- #
pwmFreq = 60
pwmI2CAddr = 0x40
pwmI2CDebug = True
# ------------------------------------- #

# ------- Servo Limits --------- #
servoLimitArmMin = 150
servoLimitArmMax = 450

servoLimitHeadRight = 220
servoLimitHeadCenter = 385
servoLimitHeadLeft = 550

servoLimitHeadUp = 410
servoLimitHeadLevel = 350
servoLimitHeadDown = 220
# ------------------------------ #

# ------- Servo Pins ----------- #
servoPinHeadPan = 2
servoPinHeadTilt = 5
servoPinArmLeft = 0
servoPinArmRight = 1
servoPinTrackLeft = 3
servoPinTrackRight = 4
# ------------------------------ #