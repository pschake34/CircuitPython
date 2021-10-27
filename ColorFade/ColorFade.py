# Paul Schakel
# Fades the colors on a neopixel in and out in a set order

import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

r = 0
g = 0
b = 0

interval = 1
trigger = False

while True:
    if not trigger: # if the colors should be fading in
        if r <= 100: # fade in red
            r += interval

        elif r >= 100 and g <= 100: # if red is faded in, fade in green
            g += interval

        elif r and g >= 100 and b <= 100: # if green and red have been faded in, fade in blue
            b += interval

        elif r and g and b >= 100: # if all the colors are faded in, fade them out
            trigger = True

    if trigger: # if the colors should be fading out
        if g and b >= 100 and r > 0: # if green, blue and red are faded in, fade our red
            r -= interval

        elif b >= 100 and r == 0 and g > 0: # if green and blue are faded in and red isn't, fade our green 
            g -= interval

        elif r == 0 and g == 0 and b > 0: # if green and red have been faded out, fade our blue
            b -= interval

        else: # if all the colors are faded our, fade them in again
            trigger = False

    dot.fill((r, g, b))
    print(r, b, g)
    time.sleep(0.02)