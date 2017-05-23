from microbit import *

class Apa:
    def __init__(self, num_leds):
        self.buffer = bytearray(4)
        self.leds = [(0xE0,0,0x0,0) for i in range(num_leds)]
        
    def write(self):
        spi.write(b'\x00\x00\x00\x00')
        for led in self.leds:
            for i in range(4):
                self.buffer[i] = led[i]
            spi.write(self.buffer)
        spi.write(b'\x00\x00\x00\x00')
            
    def set_led(self, n, intensity, r, b, g):
        self.leds[n] = (intensity, r, b,g)
       

apa = Apa(8)
spi.init()
for i in range(8):
    apa.set_led(i, 0xF0, 0x30, 0x0, 0x0)
    apa.write()
    sleep(100)
for i in range(8):
    apa.set_led(i, 0xe0, 0x00, 0x0, 0x0)
    apa.write()
    sleep(100)
 