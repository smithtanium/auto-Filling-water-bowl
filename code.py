import time
import board
import adafruit_hcsr04
import simpleio
from valvePosition import *
from LED import *
from buzzer import *
from sonar import *

# servo pin
valvePosition = valvePosition(board.D7)

# LED
LED = LED(board.D8, board.D10, board.D9)

# piezo buzzer
buzzer = buzzer(board.D11)

# sonar pin
sonar = sonar(board.D5, board.D6)
#sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        #level = 15.0 - sonar.distance
        #print((str(level) + ' cm'))
        print(str(sonar.level()) + ' cm')
        if sonar.level() < 5.0:
            valvePosition.open()
            LED.blueON()
        else:
            valvePosition.shut()
            LED.greenON()
            if sonar.level() > 12.0:
                print("Water level is too high.")
                buzzer.alarm()
                LED.redON()
                time.sleep(1)
                LED.redOFF()
                time.sleep(1)
        time.sleep(1)
    except RuntimeError:
        print("Retrying!")
        print("Value is shut.")
        valvePosition.shut()
        buzzer.alarm()
        LED.redON()
        time.sleep(1)
        LED.redOFF()
        time.sleep(1)
    time.sleep(0.1)
