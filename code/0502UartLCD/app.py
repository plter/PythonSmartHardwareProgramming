from signal import pause

import serial

s = serial.Serial("/dev/ttyUSB0", 115200)
s.write("CLR(15);DC32(0,0,'Hello',1);\r\n")

pause()
