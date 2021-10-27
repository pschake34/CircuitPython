# Paul Schakel
# Moves a servo back and forth using two wires with capacative touch

import time
import board
import pwmio
import touchio

# Initialize PWM output for the servo (on pin D5):
servo = pwmio.PWMOut(board.D5, frequency=50)

# Initialize touch sensors at A0 and A1
touch_right = touchio.TouchIn(board.A0)
touch_left = touchio.TouchIn(board.A1)

# Define variables to control the servo
pulse_ms = 1.0
increment = 0
delay = 0.005

def servo_duty_cycle(pulse_ms, frequency=50): # simplifies setting PWM duty cycle for the servo
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

while True:
    servo.duty_cycle = servo_duty_cycle(pulse_ms)   # set the position of the servo
    time.sleep(delay)

    if touch_left.value: # if left wire has been touched, turn left
        print("Moving Left")
        increment = 0.005
    elif touch_right.value: # if right wire has been touched, turn right
        print("Moving Right")
        increment = -0.005

    # if the values for the directional limits go past the capability of the servo, set them to a value before those limits
    if pulse_ms > 2.4:
        pulse_ms = 2.4
    elif pulse_ms < 0.6:
        pulse_ms = 0.6

    pulse_ms += increment
    print(pulse_ms)