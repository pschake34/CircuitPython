import time
import board
import adafruit_hcsr04
import math
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

r = 0
g = 0
b = 0

distance = 0

def fade(range0, range1, value):
    distance = range1 - range0
    color0 = abs(((value - range0) / distance) * 255)
    color1 = distance - value
    if color1 < 0:
        color1 = 0
    return color0, color1

while True:
    try:
        #print(sonar.distance)
        distance = sonar.distance

        if distance <= 5:
            r = 255
            g = 0
            b = 0
        elif distance <= 20:
            values = fade(5, 20, distance)
            b = int(values[0])
            r = int(values[1])
            g = 0
        elif distance <= 35:
            values = fade(20, 35, distance)
            g = int(values[0])
            b = int(values[1])
            r = 0
        else:
            r = 255
            g = 0
            b = 0
    except RuntimeError:
        print("Retrying...")
    
    print(r, g, b)
    dot.fill((r, g, b))
    time.sleep(0.1)