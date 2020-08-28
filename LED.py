import board
import digitalio

class LED():

    def __init__(self, redPin = None, bluePin = None, greenPin = None):
        self.L1 = digitalio.DigitalInOut(redPin)
        self.L1.direction = digitalio.Direction.OUTPUT
        self.L2 = digitalio.DigitalInOut(bluePin)
        self.L2.direction = digitalio.Direction.OUTPUT
        self.L3 = digitalio.DigitalInOut(greenPin)
        self.L3.direction = digitalio.Direction.OUTPUT

        self.L1.value = False # off
        self.L2.value = False # off
        self.L3.value = False # off

    def blueON(self):
        self.L2.value = True # on
        self.L1.value = False # off
        self.L3.value = False # off
        return self.L2, self.L1, self.L3

    def blueOFF(self):
        self.L2.value = False # off
        self.L1.value = False # off
        self.L3.value = False # off
        return self.L2, self.L1, self.L3

    def redON(self):
        self.L1.value = True # on
        self.L3.value = False # off
        self.L2.value = False # off
        return self.L2, self.L1, self.L3

    def redOFF(self):
        self.L1.value = False # off
        self.L2.value = False # off
        self.L3.value = False # off
        return self.L2, self.L1, self.L3

    def greenON(self):
        self.L3.value = True # on
        self.L1.value = False # off
        self.L2.value = False # off
        return self.L2, self.L1, self.L3

    def greenOFF(self):
        self.L3.value = False # off
        self.L1.value = False # off
        self.L2.value = False # off
        return self.L2, self.L1, self.L3
