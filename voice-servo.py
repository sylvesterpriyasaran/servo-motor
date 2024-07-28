import time
from adafruit_motor import servo
import adafruit_audio_board
import speech_recognition as sr

# Initialize PWM output on the chosen GPIO pin
pwm = pulseio.PWMOut(board.GP4, frequency=50)
my_servo = servo.Servo(pwm)

# Initialize microphone
mic = adafruit_audio_board.AudioIn(board.GP21)  # Example GPIO pin for digital audio input

# Initialize speech recognizer
recognizer = sr.Recognizer()

def move_servo(angle):
    # Convert angle (0-180 degrees) to PWM duty cycle (500-2500)
    pulse_width = int(500 + (angle / 180.0) * 2000)
    my_servo.angle = angle
    time.sleep(0.5)  # Adjust delay as necessary

def listen_for_commands():
    with mic as source:
        print("Listening for commands...")
        audio_data = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio_data)
        print("You said:", command)
        if "move to" in command:
            parts = command.split()
            angle = int(parts[-1])
            if 0 <= angle <= 180:
                move_servo(angle)
            else:
                print("Angle must be between 0 and 180 degrees.")
        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

while True:
    listen_for_commands()
