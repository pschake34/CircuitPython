# CircuitPython
The home for my Engineering III CircuitPython assignments.

## Table of Contents
* [ColorFade](#colorfade)
* [CircuitPython Servo](#circuitpython-servo)
* [CircuitPython Distance Sensor](#circuitpython-distance-sensor)

<br>
<br>

## ColorFade

### Description & Code

This first assignment of Engineering III was a fairly simple intro project. The goal was to make an RGB LED fade between colors. My version cycles linearly through the colors by first making the r value go up, then the g, then the b. After all the color values reach 100, they go down in the order r, g, b.

```Python
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
```

A trigger was used to differentiate between the fading in cycle and the fading out cycle, making it possible to use two sets of code to control the color, one after the other.

### Evidence

[Link to code](/ColorFade/ColorFade.py)

<img src="/ColorFade/images/ColorFade.gif" alt="Video of LED changing color" height=300>

### Wiring

None, the builtin LED was used for the assignment.

### Reflection

This was a nice simple assignment to get us started on the year. I had some issues initially with the logic for the program, but that was probably just because I was a little bit rusty.

<br>
<br>

## CircuitPython Servo

### Description & Code

This second assignment of the year brought in an interesting new concept: capacative touch. With capacative touch, instead of using traditional buttons for input, we could simply use wires which would provide input when touched. Our assignment was to make a servo turn right when one wire was touched and turn left when another was touched, staying still when no wires were touched.

```python
while True:
    servo.duty_cycle = servo_duty_cycle(pulse_ms)
    time.sleep(delay)

    increment = 0

    if touch_left.value:
        print("Moving Left")
        increment = 0.005
    elif touch_right.value:
        print("Moving Right")
        increment = -0.005

    if pulse_ms > 2.4:
        pulse_ms = 2.4
    elif pulse_ms < 0.6:
        pulse_ms = 0.6

    pulse_ms += increment
    print(pulse_ms)
```

The logic for the main loop was fairly simple, just checking if one of the wires was being touched and making sure the limits of the 180 degree servo weren't reached. 

### Evidence

[Link to Code](/ServoControl/ServoControl.py)

<img src="/ServoControl/images/ServoControl.gif" height=300 alt="Video of capacative touch servo control">

### Wiring

<img src="/ServoControl/wiring/wiring.png" height=300 alt="Wiring for CircuitPython Servo">

### Reflection

This second assignment was rather simple, but introduced the interesting new concept of capacative touch. While the implementation of the new technology was very simple, it led me to do some [research](https://en.wikipedia.org/wiki/Capacitive_sensing) into the concept and realize that this capacative touch is behind the most ubiquitous device of our time: the handheld smartphone. This simple fact renders capacative touch one of the most important technologies of today.

<br>
<br>

## CircuitPython Distance Sensor

### Description & Code

The next assignment was to make an LED fade between colors based on a distance read from an HC-SR04 ultrasonic sensor. First, the distance to an object was computed by an HC-SR04 distance sensor. From there, the distance was used to change the color of the LED on the Circuitpython board. The color began as solid red at 5cm then faded to blue at 20 and green at 35. 

```python
def fade(lower, upper, val):    # gives the values needed to fade two LEDs between a user set range
    real_upper = upper - lower
    result1 = (abs(val - lower) / real_upper) * 255
    result2 = 255 - result1
    print("Result 1: " + str(result1), end="\t")
    print("Result 2: " + str(result2), end="\t")
    print("Value: " + str(val), end="\n")
    return result1, result2
```

The fading was accomplished by using an equation to map values between a certain range to a range between 0 and 255. The function which accomplished this computed the value of the two colors which were being faded between and returned them. Here is an example graph of the values this function would return: 

<img src="/DistanceSensor/images/graph.png" width="500" height="300" style="border: 1px solid #ccc" frameborder=0>
<a href="https://www.desmos.com/calculator/negv6nlvij">
<img/>

### Evidence

[Link to Code](/DistanceSensor/DistanceSensor.py)

<img src="/DistanceSensor/images/DistanceSensor.gif" height=300 alt="Video of Distance Sensor">

### Wiring

<img src="/DistanceSensor/wiring/wiring.png" height=300 alt="Wiring for CircuitPython Distance Sensor">

### Reflection

This was a fun assignment for me, because making LEDs fade brings me an inordinate amount of happiness. However, I did decide to take a more complicated route than I perhaps needed to do by using algebra to map the distance values to color values. A much easier route would have been to simply use the [*simpleio library*](https://circuitpython.readthedocs.io/projects/simpleio/en/latest/api.html#simpleio.map_range) to map the values without doing the math myself. Even though this would have been easier, I'm still glad that I put the extra work in to figure out the math myself because of the added satisfaction of knowing that it was more of my code doing the heavy lifting.

