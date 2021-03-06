#usr!/bin/python3
#6.Test Motor-Driver_movement_2.3.py
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(29, gpio.OUT)
gpio.setup(31, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(36, gpio.OUT)

pwmPinR = 12
pwmPinL = 16
gpio.setup(pwmPinR,gpio.OUT)
gpio.setup(pwmPinL,gpio.OUT)
pwm1 = gpio.PWM(pwmPinR, 50)
pwm2 = gpio.PWM(pwmPinL, 50)

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
    pwm1.start(100)
    pwm2.start(100)
#    time.sleep(tf)
#    gpio.cleanup()

def backward():
#    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(7, True)
    pwm1.start(100)
    pwm2.start(100)
#    time.sleep(tf)
#    gpio.cleanup()
    
def turnright():
#    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
    pwm1.start(40)
    pwm2.start(100)
#    time.sleep(tf)
#    gpio.cleanup()

def turnleft():
#    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
    pwm1.start(100)
    pwm2.start(40)
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
import time
import tty
import sys
import termios

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	tty.setraw(sys.stdin.fileno())
	ch = sys.stdin.read(1)
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

var = "n"

##### MAIN #####
import subprocess, os, time
#init()


subprocess.call("luvcview")
#time.sleep(1)


_forward = 0
_backward = 0
_turnleft = 0
_turnright = 0

while var != "q":
    var = getch()
    if (var == "a" and _turnleft == 0):
        turnleft()
        _forward = 0
        _backward = 0
        _turnleft = 1
        _turnright = 0
        print("going left")
    if (var == "d" and _turnright == 0):
        turnright()
        _forward = 0
        _backward = 0
        _turnleft = 0
        _turnright = 1
        print("going right")
    if (var == "w" and _forward == 0):
        forward()
        _forward = 1
        _backward = 0
        _turnleft = 0
        _turnright = 0
        print("going forward")
    if (var == "s" and _backward == 0):
        backward()
        _forward = 0
        _backward = 1
        _turnleft = 0
        _turnright = 0
        print("going backward")
#    if (var != "a" or var != "d" or var != "w" or var !="s"):
#        time.sleep(0.4)
#        stop()
#        _forward = 0
#        _backward = 0
#        _turnleft = 0
#        _turnright = 0
#        print("stopping")
    if (var != "a" and var != "d" and var != "w" and var != "s"):
        stop()
        _forward = 0
        _backward = 0
        _turnleft = 0
        _turnright = 0
        print("stopping now")
    time.sleep(0.1)



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



