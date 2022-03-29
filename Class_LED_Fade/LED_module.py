# Paul Schakel
# LED_module.py

import time
import board
import pwmio

class LED:
    '''LED is a class designed for a single color LED to fade in and out'''
    
    pin = board.D0
    led = None

    def __init__(self, ledpin):
       self.pin = ledpin
       self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)

    def fade(self):
        for i in range(100):
            # PWM LED up and down
            if i < 50:
                self.led.duty_cycle = int(i * 2 * 65535 / 98)  # Up
            else:
                self.led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 98)  # Down
            time.sleep(0.01)
