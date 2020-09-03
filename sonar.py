import adafruit_hcsr04

class sonar():
    def __init__(self, sonarTriggerPin = None, sonarEchoPin = None):
        self.s1 = adafruit_hcsr04.HCSR04(sonarTriggerPin, sonarEchoPin)
        super().__init__()

    def level(self):
        level = 10.0 - self.s1.distance
        return level
