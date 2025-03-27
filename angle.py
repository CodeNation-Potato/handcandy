from gpiozero import Servo
from time import sleep
servo = Servo(17)  # Replace 17 with your GPIO pin
while True:
      angle = servo.value  # Read the servo's current angle
      print(f"Current angle: {angle:.1f} degrees")
      sleep(0.5)

