import board
import touchio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

touch_direction = touchio.TouchIn(board.A0)
touch_move = touchio.TouchIn(board.A1)

value = 0
direction_trigger = False
move_trigger = False
difference = 1

def print_output():
    if difference > 0:
        lcd.set_cursor_pos(1, 0)
        lcd.print("Direction: UP  ")
    else:
        lcd.set_cursor_pos(1, 0)
        lcd.print("Direction: DOWN")
    
    print(difference)

    lcd.set_cursor_pos(0, 0)
    lcd.print("Value: " + str(value) + " ")

while True:
    if touch_direction.value and not direction_trigger:
        difference *= -1
        direction_trigger = True
        print_output()
    elif direction_trigger and not touch_direction.value:
        direction_trigger = False

    if touch_move.value and not move_trigger:
        value += difference
        move_trigger = True
        print_output()
    elif move_trigger and not touch_move.value:
        move_trigger = False
