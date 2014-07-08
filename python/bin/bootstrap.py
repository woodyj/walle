import os
import time

print "============================================"
print "| WALL-E System Boot                       |"
print "============================================"

print "Testing servos:"
time.sleep(1)

# head
print "Head turn left..."
time.sleep(1)
print "Head turn right..."
time.sleep(1)
print "Look up..."
time.sleep(1)
print "Look down..."
time.sleep(1)

# arms
print "Left arm up..."
time.sleep(1)
print "Left arm down..."
time.sleep(1)
print "Right arm up..."
time.sleep(1)
print "Right arm down..."
time.sleep(1)

print ""
print "Testing drivetrain:"

# tracks
print "Move forward..."
time.sleep(1)
print "Move backward..."
time.sleep(1)
print "Turn left..."
time.sleep(1)
print "Turn right..."
time.sleep(1)

print ""
print "Testing eyes:"

# test eyes
print "Left eye blink..."
time.sleep(1)
print "Right eye blink..."
time.sleep(1)
print "Both eyes on..."
time.sleep(1)

print ""
print "Testing environment sensors:"

# test distance sensor
print "Testing distance sensor..."
time.sleep(1)

# test microphone
print "Testing mircrophone..."
time.sleep(1)

# test camera
print "Testing camera..."
time.sleep(1)

# test speech
print ""
print "Testing speech..."
time.sleep(1)
os.system('mpg321 ../lib/sounds/wall-e.mp3 &')
time.sleep(3)

# main control loop
print ""
print "Starting WALL-E's brain..."
time.sleep(2)
print "Uh oh!  No brain detected!"
