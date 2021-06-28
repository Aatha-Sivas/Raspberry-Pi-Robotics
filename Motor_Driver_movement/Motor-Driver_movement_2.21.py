#usr!/bin/python3
#6.Test Motor-Driver_movement_2.21.py
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
import subprocess, os, time
init()

screen = display.set_mode ((1, 1))
display.set_caption("ROVER MOVING PROGRAM")
#subprocess.call("luvcview")
#time.sleep(1)

endProgram = False

_forward = 0
_backward = 0
_turnleft = 0
_turnright = 0

while not endProgram:
    for e in event.get():
        if (e.type == KEYDOWN):
            if (e.key == K_LEFT and _turnleft == 0):
                turnleft()
                _forward = 0
                _backward = 0
                _turnleft = 1
                _turnright = 0
                print ("going left")
#                time.sleep(0.01)
            if (e.key == K_RIGHT and _turnright == 0):
                turnright()
                _forward = 0
                _backward = 0
                _turnleft = 0
                _turnright = 1
                print ("going right")
#                time.sleep(0.01)
            if (e.key == K_UP and _forward == 0):
                forward()
                _forward = 1
                _backward = 0
                _turnleft = 0
                _turnright = 0
                print("going forward")
#                time.sleep(0.01)
            if (e.key == K_DOWN and _backward == 0):
                backward()
                _forward = 0
                _backward = 1
                _turnleft = 0
                _turnright = 0
                print ("going backward")
#                time.sleep(0.01)
            if (e.key != K_LEFT and e.key != K_RIGHT and e.key != K_UP and e.key != K_DOWN):
                _forward = 0
                _backward = 0
                _turnleft = 0
                _turnright = 0
                stop()
                print ("stopping")
#            if (_forward == 1 or _backward == 1 or _turnleft == 1 or turnright == 1):
#                time.sleep(1)
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



