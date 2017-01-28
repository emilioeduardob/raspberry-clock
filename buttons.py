#5  X Button
#23 #Circle Button for GPIO23
#22 #Square Button for GPIO22
#24 #Trigon Button for GPIO24
#5 #X Button for GPIO5
#4 #R (side) Button for GPIO4
#17 #Trigon (power) Button for GPIO4
# 27 Screen
import RPi.GPIO as GPIO
import lcd

LCD = lcd.Lcd()

print '-- Initializing buttons'
GPIO.setmode(GPIO.BCM)

def handle_button(button):
    if button == 5:
        LCD.toggle()

buttons = [5, 23, 22, 24, 4, 17]

for button in buttons:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(button, GPIO.RISING, callback=handle_button, bouncetime=100)
