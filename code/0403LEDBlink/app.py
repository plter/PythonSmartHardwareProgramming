from signal import pause
from time import sleep

from gpiozero import LED

l = LED(17)

# while True:
#     l.on()
#     sleep(1)
#     l.off()
#     sleep(1)

l.blink()
pause()
