#!/usr/bin/env python

import RPI.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('What do you want to write?')
    reader.write(text)
    print("Write complete")
finally:
    GPIO.cleanup()

