import wiringpi, numpy

wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetup(0, 500000)

data = bytearray(4)
# data[0] = ~numpy.uint8(0b00000001)
# data[1] = ~numpy.uint8(0b00000000)
# data[2] = ~numpy.uint8(0b00000000)
# data[3] = 0b00000001
t_data = bytearray(8)
t_data[0] = 0b11111111
t_data[1] = 0b11111111
t_data[2] = 0b00011000
t_data[3] = 0b00011000
t_data[4] = 0b00011000
t_data[5] = 0b00011000
t_data[6] = 0b00011000
t_data[7] = 0b00011000

while True:
    for i in range(0, 8):
        data[0] = ~numpy.uint8(t_data[i])
        data[1] = ~numpy.uint8(0b00000000)
        data[2] = ~numpy.uint8(0b00000000)
        data[3] = 1 << i
        wiringpi.wiringPiSPIDataRW(0, bytes(data))
