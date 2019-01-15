#!/usr/bin/python
#
# Open shutter script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import serial
import time

DOME='/dev/Dome'
status=0
# Ouverture des portes
ser=serial.Serial(DOME)
time.sleep(2)
ser.flush()
ser.write(b'P+#')

#rep=ser.readline().strip()
rep=ser.read(1)
if (rep==b"1"):
    ret=" 1 "
else:
    ret=" 0 "
    status=1

coordinates = open('/tmp/indi-status', 'r')
str = coordinates.readline()
coordinates.close()
str = str[0] + ret + str[4:]
coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write(str)
coordinates.close()

sys.exit(status)
