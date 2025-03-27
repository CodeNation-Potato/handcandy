#1.Need way to check current position of the servo motor
#2.Force the motor to switch to 90 degrees
#3.Have the motor turn 180 degrees, pause for 2 seconds and go back to orginal position
#4 1-3 must be done when an open palm is detected. Need to use time.sleep to check for a hand and after two seconds of hand checking, the motor will move
#5 Must move back and ignore the open palm of the hand until the motor goes back to original position and process repeats

#New Idea, one big while loop where position is checked, moved to 90 and nested within for loop of video stream. 
