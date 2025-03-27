from gpiozero import AngularServo
from time import sleep

# Initialize the servo on a specific GPIO pin
servo = AngularServo(17, min_angle=0, max_angle=180)

# Variable to keep track of the current angle
current_angle = 0

def turn_servo_by(angle):
    global current_angle
    new_angle = current_angle + angle
    
    # Ensure the new angle is within the servo's limits
    if new_angle < 0 or new_angle > 180:
        print("Angle out of bounds. Please provide a valid angle.")
        return
    
    # Check if the servo is already at the new angle
    if current_angle == new_angle:
        print(f"Servo is already at {current_angle} degrees. No movement needed.")
        return
    
    # Set the servo to the new angle
    servo.angle = new_angle
    current_angle = new_angle
    print(f"Servo turned to {current_angle} degrees.")
    
    # Optional: Wait for the servo to reach the position
    sleep(1)

# Example usage
turn_servo_by(90)  # First turn to 90 degrees
turn_servo_by(90)  # Attempt to turn to 180 degrees
turn_servo_by(-90) # Turn back to 90 degrees
turn_servo_by(-90) # Attempt to turn back to 0 degrees
