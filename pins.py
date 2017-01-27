import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Circle Button for GPIO23
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Square Button for GPIO22
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Trigon Button for GPIO24
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) #X Button for GPIO5
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #R (side) Button for GPIO4
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Trigon (power) Button for GPIO4

active = True
prev_input = 0

while True:
  input = GPIO.input(5)
  if ((not prev_input) and input):
    print("Button Pressed")
    if (active):
      active = False
      GPIO.setup(27, GPIO.OUT)
    else:
      active = True
      GPIO.setup(27, GPIO.IN)
  prev_input = input
  time.sleep(0.05)
