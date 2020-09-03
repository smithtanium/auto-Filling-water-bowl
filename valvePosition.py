#import pulseio
#import simpleio
import digitalio
#from adafruit_motor import servo

class valvePosition():

    def __init__(self, relayPin = None):
        self.V1 = digitalio.DigitalInOut(relayPin)
        self.V1.direction = digitalio.Direction.OUTPUT
        self.V1.value = False


    def shut(self):
        self.V1.value = False
        return self.V1.value

    def open(self):
        self.V1.value = True
        return self.V1.value
