import sys

print "Press a key, then press enter:"

while True:
    char = sys.stdin.read(1)
    print 'You pressed %s' % char