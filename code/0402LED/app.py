from gpiozero import LED
from time import sleep

l = LED(17)
l.on()

sleep(3)
