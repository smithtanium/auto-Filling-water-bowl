import pulseio
import simpleio
import digitalio
from adafruit_motor import servo

class valvePosition(servo.Servo):

    def __init__(self, servoPin = None):
        self.pwm = pulseio.PWMOut(servoPin, duty_cycle=2 ** 15, frequency=50)
        super().__init__(self.pwm)
        my_servo = servo.Servo(self.pwm)
        self.angle = 0

    def shut(self):
        self.angle = 90
        return self.angle

    def open(self):
        self.angle = 0
        return self.angle
