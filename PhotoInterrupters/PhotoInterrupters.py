import time
import board
from digitalio import DigitalInOut, Direction, Pull

interrupter = DigitalInOut(board.D10)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP
timesInterrupted = 0

triggered = False
state = False

while True:
    elapsed = time.monotonic()
    triggered = interrupter.value

    if elapsed % 4 == 0:
        print("The number of interrupts is: " + str(timesInterrupted))

    if triggered and not state:    # if the interrupter is triggered and hasn't already been triggered
        timesInterrupted += 1
        state = True
    elif state and not triggered:     # if the interrupter isnt triggered, update the state
        state = False