#usr!/bin/python3
#6.Test Motor-Driver_movement_3.py
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
import lirc
sockid = lirc.init("irexec")

##### MAIN #####


_forward = 0
_backward = 0
_turnleft = 0
_turnright = 0

while True:
    try:
        button = lirc.nextcode()
        if (button == KEY_LEFT and _turnleft == 0):
            turnleft()
            _forward = 0
            _backward = 0
            _turnleft = 1
            _turnright = 0
        if (button == KEY_RIGHT and _turnright == 0):
            turnright()
            _forward = 0
            _backward = 0
            _turnleft = 0
            _turnright = 1
        if (button == KEY_UP and _forward == 0):
            forward()
            _forward = 1
            _backward = 0
            _turnleft = 0
            _turnright = 0                
        if (button == KEY_DOWN and _backward == 0):
            backward()
            _forward = 0
            _backward = 1
            _turnleft = 0
            _turnright = 0
        if (button != KEY_LEFT and button != KEY_RIGHT and button != KEY_UP and button != KEY_DOWN):
            _forward = 0
            _backward = 0
            _turnleft = 0
            _turnright = 0
            stop()
        time.sleep(0.1)
    except KeyboardInterrupt:
        lirc.deinit()
        stop()
        break
    
gpio.cleanup()
