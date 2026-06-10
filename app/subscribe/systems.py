import time 

import RPi.GPIO as GPIO


# Setup for Raspberry Pi
relay = 18
switch = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def on():
    """Turns physical system on.
    """
    high = False
    low = False
    GPIO.output(relay, True)
    while True:
        i = GPIO.input(switch)
        if (i == 0):
            low = True
            time.sleep(0.1)
        elif (i == 1):
            high = True
            time.sleep(0.1)
        if high and not low:
            high = False
        elif high and low:
            GPIO.output(relay, False)
            return


def off():
    """Turns physical system off.
    """
    high = False
    low = False
    GPIO.output(relay, True)
    while True:
        i = GPIO.input(switch)
        if (i == 0):
            low = True
            time.sleep(0.1)
        elif (i == 1):
            high = True
            time.sleep(0.1)
        if low and not high:
            low = False
        elif high and low:
            GPIO.output(relay, False)
            return
