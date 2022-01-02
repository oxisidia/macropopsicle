"""Macropopsicle Keypad Code"""
#This code was originally published by Adafruit.
#It was modified by Dylan Rice.
#If using this code in whole or in part please include attribution to all prior authors.

import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# A simple neat keyboard demo in CircuitPython

# The pins we'll use, each will have an internal pullup resistor.
keypress_pins = [board.A0, board.A1]

# Our array of key objects
key_pin_array = []


# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.ONE, Keycode.TWO]

control_key = Keycode.SHIFT


# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems

keyboard = Keyboard(usb_hid.devices)

keyboard_layout = KeyboardLayoutUS(keyboard)


# Make all pin objects inputs with pullups
for pin in keypress_pins:

    key_pin = digitalio.DigitalInOut(pin)

    key_pin.direction = digitalio.Direction.INPUT

    key_pin.pull = digitalio.Pull.UP

    key_pin_array.append(key_pin)

while True:

    # Check each pin
    for key_pin in key_pin_array:

        if not key_pin.value:  # Is the key pin grounded?

            i = key_pin_array.index(key_pin) #set i equal to the key pin array index.

            while not key_pin.value:

                pass  # Wait for it to be ungrounded!

            # "Type" the Keycode or string
            key = keys_pressed[i]  # Get the corresponding Keycode or string

            if isinstance(key, str):  # If it's a string...

                keyboard_layout.write(key)  # ...Print the string

            else:  # If it's not a string...

                keyboard.press(key)

                keyboard.release_all()  # ..."Release"!

    time.sleep(0.01)