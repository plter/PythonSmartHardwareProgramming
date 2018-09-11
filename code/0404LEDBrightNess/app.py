from signal import pause
from time import sleep

from gpiozero import PWMLED

l = PWMLED(17)

# for i in range(0, 100):
#     v = float(i) / 100
#     print v
#     l.value = v
#     sleep(0.1)

l.pulse()
pause()
