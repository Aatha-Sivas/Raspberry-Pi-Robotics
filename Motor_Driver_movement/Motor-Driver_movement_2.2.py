#usr!/bin/python3
#6.Test Motor-Driver_movement_2.2.py
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(29, gpio.OUT)
gpio.setup(31, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(36, gpio.OUT)

#def init():
#    gpio.setmode(gpio.BOARD)
#    gpio.setup(13, gpio.OUT)
#    gpio.setup(15, gpio.OUT)
#    gpio.setup(29, gpio.OUT)
#    gpio.setup(31, gpio.OUT)
#    gpio.setup(7, gpio.OUT)
#    gpio.setup(36, gpio.OUT)
    
def forward():
#    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
#    time.sleep(tf)
#    gpio.cleanup()

def backward():
#    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(7, True)
#    time.sleep(tf)
#    gpio.cleanup()
    
def turnright():
#    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, False)
    gpio.output(31, False)
    gpio.output(7, True)
#    time.sleep(tf)
#    gpio.cleanup()

def turnleft():
#    init()
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
#    time.sleep(tf)
#    gpio.cleanup()

def stop():
#    init()
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(29, False)
    gpio.output(31, False)
#    gpio.output(36, True)
#    time.sleep(tf)
#    gpio.cleanup()

#### Keypress ###
from pygame import *

##### MAIN #####

init()

screen = display.set_mode ((1, 1))
display.set_caption("ROVER MOVING PROGRAM")

endProgram = False

_forward = 0
_backward = 0
_turnleft = 0
_turnright = 0

while not endProgram:
    for e in event.get():
        if (e.type == KEYDOWN):
            if (e.key == K_a and _turnleft == 0):
                turnleft()
                _forward = 0
                _backward = 0
                _turnleft = 1
                _turnright = 0
                print("going left")
            if (e.key == K_d and _turnright == 0):
                turnright()
                _forward = 0
                _backward = 0
                _turnleft = 0
                _turnright = 1
                print("going right")
            if (e.key == K_w and _forward == 0):
                forward()
                _forward = 1
                _backward = 0
                _turnleft = 0
                _turnright = 0
                print("going forward")
            if (e.key == K_s and _backward == 0):
                backward()
                _forward = 0
                _backward = 1
                _turnleft = 0
                _turnright = 0
                print("going back")
            if (e.key != K_a and e.key != K_d and e.key != K_w and e.key != K_s):
                _forward = 0
                _backward = 0
                _turnleft = 0
                _turnright = 0
                stop()
                print("stopping")
#            if (_forward == 1 or _backward == 1 or _turnleft == 1 or _turnright == 1):
#                _forward = 0
#                _backward = 0
#                _turnleft = 0
#                _turnright = 0
#                stop()
                print("HOLD UP")
            if (e.key == K_ESCAPE):
                endProgram = True
                stop()

gpio.cleanup()


#print("forward")
#forward(3)
#print("backward")
#backward(2)
#print("Turn Right")
#turnright(2)
#print("Turn Left")
#turnleft(3)

print("Task Done")

#gpio.setmode(gpio.BOARD)
#gpio.setup(12, gpio.OUT)
#gpio.output(12, True)
#time.sleep(3)
#gpio.cleanup()



