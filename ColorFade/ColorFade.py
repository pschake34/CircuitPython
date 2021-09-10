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
    if not trigger:
        if r <= 100:
            r += interval

        elif r >= 100 and g <= 100:
            g += interval

        elif r and g >= 100 and b <= 100:
            b += interval

        elif r and g and b >= 100:
            trigger = True

    if trigger:
        if g and b >= 100 and r > 0:
            r -= interval

        elif b >= 100 and r == 0 and g > 0:
            g -= interval

        elif r == 0 and g == 0 and b > 0:
            b -= interval

        else:
            trigger = False

    dot.fill((r, g, b))
    print(r, b, g)
    time.sleep(0.02)