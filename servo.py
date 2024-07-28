from machine import Pin, PWM
from time import sleep


# Define the GPIO pin where the signal wire is connected
servo_pin = 3

# Initialize PWM on the selected GPIO pin
pwm = PWM(Pin(servo_pin))

# Set the PWM frequency to 50 Hz (standard for servos)
pwm.freq(50)

def setServoCycle(position):
    pwm.duty_u16(position)
    sleep(0.02)

while True:
    for pos in range(1000, 9000, 50):
        print("right")
        setServoCycle(pos)
    for pos in range(8000, 1000, -50):
        print("left")
        setServoCycle(pos)
