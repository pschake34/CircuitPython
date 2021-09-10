import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

r = 0
g = 0
b = 0

interval = 3
trigger = False

while True:
    if r <= 100:
        r += interval

    elif r >= 100 and g <= 100:
        g += interval

    elif r and g >= 100 and b <= 100:
        b += interval

    elif r and g and b >= 100 and trigger == False:
        trigger = True

    if trigger:
        if g and b >= 100:
            r -= interval

        elif b >= 100:
            g -= interval

        elif r and g < 100:
            b -= 100

        else:
            trigger = False

    dot.fill((r, g, b))
    print(r, b, g)