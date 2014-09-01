import _config_
import time
from models.drivers.pwm.Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(_config_.pwmI2CAddr, debug=_config_.pwmI2CDebug)
pwm.setPWMFreq(_config_.pwmFreq)

i = 1;
while (i > 0):
  # Change position of servo on channel O (left arm)
  pwm.setPWM(1, 0, _config_.servoArmMin)
  time.sleep(1)
  pwm.setPWM(1, 0, _config_.servoArmMin)
  time.sleep(1)
  i -= 1