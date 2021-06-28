#usr!/bin/python3
#3.Test Motor-Driver_3.py
import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(29, gpio.OUT)
    gpio.setup(31, gpio.OUT)

def turnright(tf):
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, False)
    gpio.output(31, True)
    time.sleep(tf)
    gpio.cleanup()

def turnleft(tf):
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, True)
    gpio.output(31, False)
    time.sleep(tf)
    gpio.cleanup()
    
print("Turn Right")
turnright(2)
print("Turn Left")
turnleft(4)

print("Task Done")
