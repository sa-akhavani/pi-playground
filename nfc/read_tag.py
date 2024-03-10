#!/usr/bin/env python

import RPI.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print(id, text)
finally:
    GPIO.cleanup()

