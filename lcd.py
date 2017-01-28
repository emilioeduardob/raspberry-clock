import RPi.GPIO as GPIO

class Lcd:
    def __init__(self):
        self.active = True

    def toggle(self):
        if (self.active):
          self.active = False
          GPIO.setup(27, GPIO.OUT)
        else:
          self.active = True
          GPIO.setup(27, GPIO.IN)
