import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_ducky

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

duck = adafruit_ducky.Ducky("payload.txt", keyboard, keyboard_layout)

time.sleep(1)

result = True
count = 0 
while result is not False and count < 10:
    result = duck.loop()
    count += 1