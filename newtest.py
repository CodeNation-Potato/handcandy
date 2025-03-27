from gpiozero import AngularServo
from time import sleep

#servo = AngularServo(14, min_angle=0, max_angle=360, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
servo = AngularServo(14, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)


def set_value(angle):
    servo.value = angle
    sleep(1)

try:
    while True:
        angle = int(input("Enter an angle: "))
        set_value(angle)
except KeyboardInterrupt:
    print("Program stopped by user")
