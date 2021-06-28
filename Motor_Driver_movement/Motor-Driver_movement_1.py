#usr!/bin/python3
#5.Test Motor-Driver_movement_1.py
import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(29, gpio.OUT)
    gpio.setup(31, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    
def forward(tf):
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()

def backward(tf):
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()
    
def turnright(tf):
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()

def turnleft(tf):
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()

print("forward")
forward(3)
print("backward")
backward(2)
print("Turn Right")
turnright(2)
print("Turn Left")
turnleft(3)

print("Task Done")

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.output(12, True)
time.sleep(3)
gpio.cleanup()



