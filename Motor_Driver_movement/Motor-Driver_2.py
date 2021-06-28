#usr!/bin/python3
#2.Test Motor-Driver_2.py
import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(29, gpio.OUT)
    gpio.setup(31, gpio.OUT)

def forward(tf):
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    time.sleep(tf)
    gpio.cleanup()

def backward(tf):
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, False)
    gpio.output(31, True)
    time.sleep(tf)
    gpio.cleanup()


print("forward")
forward(4)
print("backward")
backward(2)


print("Task Done")
