from gpiozero import AngularServo
import time
from time import sleep
servo = AngularServo(14, min_pulse_width = 0.5/1000, max_pulse_width=2.5/1000)

while (True):
      servo.angle = 90
      print("Turning 90")
      sleep(2)
      print("Turning back")
      servo.angle = -90
      sleep(2)
      break
print("Finished")


