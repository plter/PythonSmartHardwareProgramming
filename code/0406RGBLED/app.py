from signal import pause
from time import sleep

from gpiozero import RGBLED

l = RGBLED(13, 19, 26)

while True:
    l.value = (1, 0, 0)
    sleep(1)
    l.value = (0, 1, 0)
    sleep(1)
    l.value = (0, 0, 1)
    sleep(1)
    l.value = (1, 1, 0)
    sleep(1)
    l.value = (0, 1, 1)
    sleep(1)
    l.value = (1, 0, 1)
    sleep(1)
    l.value = (1, 1, 1)
    sleep(1)
