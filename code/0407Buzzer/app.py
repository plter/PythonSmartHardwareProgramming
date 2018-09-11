from signal import pause
import pygame

# from gpiozero import Buzzer
#
# b = Buzzer(6)
#
# b.blink(0.0001, 0.0001)
#
# pause()


pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

pause()
