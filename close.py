#!/usr/bin/python
#
# Close shutter script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import time
import serial

DOME='/dev/Dome'
status=0

# Fermeture des portes
ser=serial.Serial(DOME)
time.sleep(2)
ser.flush()
ser.write(b'P-#')

# TODO Attente portes fermees
#rep=ser.readline().strip()
rep=ser.read(1)
if (rep==b"1"):
    ret=" 0 "
else:
    ret=" 1 "
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

