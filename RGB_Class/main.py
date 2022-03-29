''' This file is the class-based version of making a single LED fade'''
import time
import board
from rgb import RGB

r1 = board.D10
g1 = board.D9
b1 = board.D8
r2 = board.D7
g2 = board.D5
b2 = board.D4

full = 65535                # Max Brightness
half = int(65535/2)         # Half Brightness

myRGBled1 = RGB(r1, g1, b1) # create a new RGB object, using pins 8, 9, & 10
myRGBled2 = RGB(r2, g2, b2) # create a new RGB object, using pins 4, 5, & 7


while True:
    '''Shines two RGB LEDs in opposing colours, then rainbows!'''
    
    print("cycle")
    myRGBled1.blue(half)
    myRGBled2.yellow(half)
    time.sleep(2)
    myRGBled1.off()
    myRGBled2.off()

    myRGBled1.red(half)
    myRGBled2.cyan()
    time.sleep(2)
    myRGBled1.off()
    myRGBled2.off()

    myRGBled1.green(half)
    myRGBled2.magenta()
    time.sleep(2)
    myRGBled1.off()
    myRGBled2.off()

    myRGBled1.blinky(1.3) # Obviously you should replace "rate1" with a real number...
    myRGBled2.blinky(1.75) # Sames
    time.sleep(1)

    # extra spicy (optional):
    myRGBled1.rainbow(0.1) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
    myRGBled2.rainbow(0.05) # Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
    time.sleep(2)

