#!/usr/bin/python3
#
# Connect script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import time
import serial

DOME='/dev/Dome'
# Lecture de l'etat du dome et mise a jour du pilote Indi

ser=serial.Serial(DOME)
time.sleep(2)
ser.flush()
ser.write(b'P?#')
rep=ser.readline().strip()
print(rep)
if rep==b'1':
    retP='1'
else:
    retP='0'
ser.write(b'D?#')
rep=ser.readline().strip()
if rep==b'1':
    retD='0'
else:
    retD='1'
coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write(retD+' '+retP+' 0')
coordinates.close()

sys.exit(0)
