import time
import board
from LED_module import LED   # import the RGB class from the rgb module

redLEDPin = board.D3
#greenLEDPin = board.D5
blueLEDPin = board.D5

myRedLED = LED(redLEDPin)
#myGreenLED = LED(greenLEDPin)
myBlueLED = LED(blueLEDPin)

while True:
    myBlueLED.fade()
    time.sleep(1)
    myRedLED.fade()
    time.sleep(1)