# 5  X Button
# 23 #Circle Button for GPIO23
# 22 #Square Button for GPIO22
# 24 #Trigon Button for GPIO24
# 5 #X Button for GPIO5
# 4 #R (side) Button for GPIO4
# 17 #Trigon (power) Button for GPIO4
# 27 Screen
from gpiozero import Button
import lcd

LCD = lcd.Lcd()

x_button = Button(5)
x_button.when_pressed = LCD.toggle
