import simpleio

class buzzer():
    def __init__(self, buzzerPin):
        self.b1 = buzzerPin

    def alarm(self):
        self.buzzer = simpleio.tone(self.b1, 440, duration=1.0)
        return self.buzzer
