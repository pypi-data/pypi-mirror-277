import time
from inventorhatmini import InventorHATMini, NUM_MOTORS  # , MOTOR_A, MOTOR_B
# from ioexpander.common import REVERSED_DIR

"""
Demonstrates how to read the angles of Inventor HAT Mini's two motor encoders.

Press "User" to exit the program.
"""

# Constants
NAMES = ["A", "B"]      # Friendly names to give the encoders
GEAR_RATIO = 50         # The gear ratio of the motor

# Create a new InventorHATMini
board = InventorHATMini(motor_gear_ratio=GEAR_RATIO, init_leds=False)

# Uncomment the below lines (and the top imports) to
# reverse the counting direction of an encoder
# board.encoders[MOTOR_A].direction(REVERSED_DIR)
# board.encoders[MOTOR_B].direction(REVERSED_DIR)

# Read the encoders until the user button is pressed
while not board.switch_pressed():

    # Print out the angle of each encoder
    for i in range(NUM_MOTORS):
        print(NAMES[i], "=", board.encoders[i].degrees(), end=", ")
    print()

    time.sleep(0.1)
