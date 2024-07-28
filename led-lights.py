from picozero import LED
from time import sleep

yellow = LED(13)

while True:
    yellow.on()
    sleep(0.1)
    yellow.off()
    sleep(0.2)
