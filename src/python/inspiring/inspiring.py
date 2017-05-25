from microbit import *

# the API is likely to change, and may change in ways that break existing code.

class Apa:
    def __init__(self, num_leds):
        self.buffer = bytearray(4)
        self.leds = [bytearray([0xE0,0,0x0,0]) for i in range(num_leds)]
        
    def show(self):
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

    # allow indexing
    def __getitem__(self, item):
        return self.leds[item]

    # allow indexed assignment
    def __setitem__(self, key, value):
        self.set_led(key, *value)

    # low-level set method allows default intensity, adjusts intensity value
    def set_led(self, n, r, b, g, intensity=15):
        self.leds[n][0] = self.limit(intensity)
        self.leds[n][1] = r
        self.leds[n][2] = b
        self.leds[n][3] = g        

def blue_demo():
    # bar has 8 leds
    apa = Apa(8)

    # initialise the SPI bus using defaults.
    # Pin 13 of the microbit is therefore used as CI (SCLCK) - the clock
    # Pin 15 of the microbit is used as DI (MOSI) - the data

    spi.init()

    # turn each LED blue

    for i in range(8):
        apa[i] = (0x30, 0x0, 0x0, 10)
        apa.show()
        sleep(100)
    # turn each LED off

    for i in range(8):
        apa[i] = (0x0, 0x0, 0x0, 0x0)
        apa.show()
        sleep(100)
        
def multi_colours():
    num_leds = 8
    apa = Apa(8)
    spi.init()
    # repeat until button A is pressed
    while button_a.get_presses() == 0:
        for i in range(num_leds):
            apa.set_led(i, 0xFF, 0 ,0)
            apa.show()
            sleep(100)
            apa.set_led(i, 0, 0xFF ,0)
            apa.show()
            sleep(100)
            apa.set_led(i, 0, 0 ,0xFF)
            apa.show()
            sleep(100)
            apa.set_led(i, 0, 0, 0, 0)
            apa.show()
            sleep(100)

if __name__ == '__main__':
    #blue_demo()
    multi_colours()

