from gpiozero import LED, Button

l = LED(17)
b = Button(27)

while True:
    b.wait_for_active()
    l.toggle()
    b.wait_for_inactive()
