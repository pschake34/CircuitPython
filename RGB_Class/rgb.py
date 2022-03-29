# These are the libraries needed to fade an LED, even if you imported elsewhere
import time
import board
import pwmio
import digitalio

lightBulb = digitalio.DigitalInOut(board.D13)       # I moved my RGBLED power wire from 5v
lightBulb.direction = digitalio.Direction.OUTPUT    # and plugged it into D13.  I'll explain later.

class LED:      # It's propper coding to always write a line explaining a class
                # with a "docstring."   Like this:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin, name):
        # init is like void Setup() from arduino.  Initialize your pins here
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)
        self.name = name

    def fadedown(self): # Fades LED from bright to dim
        for i in range(255):
            if i < (255/2):
                self.led.duty_cycle = int(i * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def fadeup(self):  # Fades LED from dim to bright
        for i in range(255):
            if i > (255/2):
                self.led.duty_cycle = 65535 - int((i - (255/2)) * 65535 / (255/2))
            print(self.name, ", ", self.led.duty_cycle)
            time.sleep(0.01)

    def on(self, brightness=65535):  # Remember "on" means duty cycles < 65535
        print("brightness: ")
        print(brightness)
        self.led.duty_cycle = 65535 - brightness
        lightBulb.value = 65535


    def off(self): # "off" means duty cycle should be full.
        self.led.duty_cycle = 65535



class RGB:
    '''this class should impliment all 3 pins together to control an RGB LED'''
    from rgb import LED
        # Let's take a second to appreciate that we're using a class to call a class!
        # Let LED do all the nitty gritty work, this RGB class will be the "manager"


    def __init__(self, redPin, greenPin, bluePin):
        # To initialize an RGB LED, we need to initialize 3 LED pins.
        self.myRedLED = LED(redPin, "red")
        self.myBlueLED = LED(bluePin, "blue")
        self.myGreenLED = LED(greenPin, "green")

    def red(self, brightness=65535):
        print("red")
        self.myRedLED.on(brightness)
        self.myGreenLED.off()
        self.myBlueLED.off()

    def green(self, brightness=65535):
        print("green")
        self.myGreenLED.on(brightness)
        self.myRedLED.off()
        self.myBlueLED.off()

    def blue(self, brightness=65535):
        print("blue")
        # Notice the brightness=65535?  Thats an OPTIONAL parameter!  So in main.py,
        # you can call "RGBLED1.blue() for full brightness, or "RGBLED1.blue(half) to
        # make it dimmer!
        self.myBlueLED.on(brightness)
        self.myGreenLED.off()
        self.myRedLED.off()

    def yellow(self, brightness=65535):
        print("yellow")
        self.myRedLED.on(int(brightness/2))
        self.myGreenLED.on(int(brightness/2))
        self.myBlueLED.off()

    def cyan(self, brightness=65535):
        print("cyan")
        self.myBlueLED.on(int(brightness/2))
        self.myGreenLED.on(int(brightness/2))
        self.myRedLED.off()

    def magenta(self, brightness=65535):
        print("magenta")
        self.myBlueLED.on(int(brightness/2))
        self.myRedLED.on(int(brightness/2))
        self.myGreenLED.off()

    def blinky(self, rate=1.25):
        i = 10000
        while i > 0:
            self.red(i)
            time.sleep(i/5000)
            i = int(i / rate)
            self.blue(i)
            time.sleep(i/5000)
            i = int(i / rate)
        self.off()

    def rainbow(self, rate=0.2):
        r = 1
        g = 1
        b = 1
        interval = 1
        trigger = False

        while True:
            print(str(r) + " " + str(g) + " " + str(b))
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
                if g and b >= 100 and r > 1: # if green, blue and red are faded in, fade our red
                    r -= interval
                elif b >= 100 and r ==1 and g >1: # if green and blue are faded in and red isn't, fade our green 
                    g -= interval
                elif r == 1 and g == 1 and b > 1: # if green and red have been faded out, fade our blue
                    b -= interval
                else: # if all the colors are faded out, stop
                    break
            
            self.myRedLED.on(int(65535*(r/1000)))
            self.myGreenLED.on(int(65535*(g/1000)))
            self.myBlueLED.on(int(65535*(b/1000)))
            time.sleep(rate)
        self.off()

    def off(self):
        # This turns off all 3 LEDs, but my LEDs were still glowing a tiny bit.
        # To fix this, i took the RGB power wire out of 5V , and plugged it into D13.
        # Now when I want the LED to be off, it's truly off!
        self.myBlueLED.off()
        self.myGreenLED.off()
        self.myRedLED.off()
        lightBulb.value = 0