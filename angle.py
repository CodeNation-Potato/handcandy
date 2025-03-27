mport RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the servo
servo_pin = 14

# Setup GPIO mode and pin
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM instance (50Hz for SG90 servo)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz PWM

# Function to set servo angle
def set_angle(angle):
    duty = angle / 18 + 2  # Calculate duty cycle (empirically determined)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Allow servo to move
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0) #Stop sending signal to allow the servo to rest and prevent jitter.

try:
    pwm.start(0) #Start PWM with 0 duty cycle.

    # Example usage:
    set_angle(0)  # Move to 0 degrees
    time.sleep(1)
    set_angle(90)  # Move to 90 degrees
    time.sleep(1)
    set_angle(180) # Move to 180 degrees
    time.sleep(1)
    set_angle(0) #Return to 0 degrees.
    time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    pwm.stop()
    GPIO.cleanup()  # Clean up GPIO settings
