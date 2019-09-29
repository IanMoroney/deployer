#!/usr/bin/env python3

from gpiozero import LEDBoard, ButtonBoard, Button, CPUTemperature
from subprocess import check_call
from signal import pause
from time import sleep
from lcd import LCD_HD44780_I2C
from rgb import Color, RGBButton
from datetime import datetime
from pprint import pprint


import socket

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/martinwoodward/DasDeployer.git"

TITLE = ">>> Das Deployer <<<"

# Define controls
lcd = LCD_HD44780_I2C()
rgbmatrix = RGBButton()
buildNumber = ""
activeEnvironment = "Dev"
pipes = None

## Nifty get_ip function from Jamieson Becker https://stackoverflow.com/a/28950776
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():

    # Quick init sequence to show all is well
    lcd.message = TITLE + "\n\n\n" + get_ip()
   # leds.blink(0.5,0.5,0,0,2,True)
    rgbmatrix.pulseButton(Color.RED, 1)
    rgbmatrix.unicornRing(25)
    sleep(8)
    lcd.message = TITLE
    lcd.clear(False)
    rgbmatrix.off()
main()

