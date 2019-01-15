#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Park script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

# Script de gestion de l'abri
# Ouverture de l'abri

import os
import sys
import serial
import time

DOME='/dev/Dome'
status=0

# Fermeture de l'abri
ser=serial.Serial(DOME)
time.sleep(2)
ser.flush()
ser.write(b'D-#')
rep=ser.read(1)
if (rep==b"1"):
    ret="1"
else:
    ret="0"
    status=1

#os.system("/usr/local/bin/park.py &")

coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write(ret+' 0 0')
#coordinates.write('1 0 0')
coordinates.close()

sys.exit(status)
