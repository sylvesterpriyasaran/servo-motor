from machine import Pin
from time import sleep

pin17 = Pin(17, Pin.OUT)


while True:
    pin17.value(1)