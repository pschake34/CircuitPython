# CircuitPython
The home for my Engineering III CircuitPython assignments.

## Table of Contents
* [ColorFade](#colorfade)
* [CircuitPython Servo](#circuitpython-servo)
* [CircuitPython LCD](#circuitpython-lcd)

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

<img src="/images/gifs/ColorFade.gif" alt="Video of LED changing color" height=300>

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

<img src="/images/gifs/ServoControl.gif" height=300 alt="Video of capacative touch servo control">

### Wiring



### Reflection
