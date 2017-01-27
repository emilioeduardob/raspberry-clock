import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
