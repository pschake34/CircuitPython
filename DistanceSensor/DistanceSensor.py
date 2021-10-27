# Paul Schakel
# Changes the color of an LED based on the distance of an object

import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

r = 0
g = 0
b = 0

distance = 0

def fade(lower, upper, val):    # gives the values needed to fade two LEDs between a user set range
    real_upper = upper - lower
    result1 = (abs(val - lower) / real_upper) * 255
    result2 = 255 - result1
    print("Result 1: " + str(result1), end="\t")
    print("Result 2: " + str(result2), end="\t")
    print("Value: " + str(val), end="\n")
    return result1, result2
    

while True:
    try:
        distance = sonar.distance

        if distance <= 5:   # makes LED red when distance <= 5
            r = 255
            g = 0
            b = 0
        elif distance <= 20:    # makes LED fade from red to blue while distance is between 5 and 20
            values = fade(5, 20, distance)
            b = int(values[0])
            r = int(values[1])
            g = 0
        elif distance <= 35:    # makes LED fade from blue to green when distance between 20 and 35
            values = fade(20, 35, distance)
            g = int(values[0])
            b = int(values[1])
            r = 0
        else:       # makes LED green when distance > 35
            r = 0
            g = 255
            b = 0
    except RuntimeError:
        print("Retrying...")
    
    print(r, g, b)
    dot.fill((r, g, b))
    time.sleep(0.1)