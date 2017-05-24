from microbit import *

# the API is likely to change, and may change in ways that break existing code.

class Apa:
    def __init__(self, num_leds):
        self.buffer = bytearray(4)
        self.leds = [bytearray([0xE0,0,0x0,0]) for i in range(num_leds)]
        
    def write(self):
        spi.write(b'\x00\x00\x00\x00')
        for led in self.leds:
            for i in range(4):
                self.buffer[i] = led[i]
            spi.write(self.buffer)
        spi.write(b'\x00\x00\x00\x00')
        
    def limit(self, intensity):
        # intensity ranges from 0 (off) to 31 (very bright)
        # but leading three bits must be set to 1, so add 0xE0
        offset = 0xE0
        if intensity < 0: return offset
        if intensity > 31: return offset + 31
        return offset + intensity
            
    def set_led(self, n, intensity, r, b, g):
        self.leds[n][0] = self.limit(intensity)
        self.leds[n][1] = r
        self.leds[n][2] = b
        self.leds[n][3] = g        
        
       
# bar has 8 leds
apa = Apa(8)

# initialise the SPI bus using defaults.
# Pin 13 of the microbit is therefore used as CI (SCLCK) - the clock
# Pin 15 of the microbit is used as DI (MOSI) - the data

spi.init()

# turn each LED blue

for i in range(8):
    apa.set_led(i, 10, 0x30, 0x0, 0x0)
    apa.write()
    sleep(100)
# turn each LED off

for i in range(8):
    apa.set_led(i, 0, 0x00, 0x0, 0x0)
    apa.write()
    sleep(100)
 