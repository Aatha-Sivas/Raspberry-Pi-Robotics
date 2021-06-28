#!usr/bin/python3
#Lightindicator lightindicator.py
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)
gpio.output(7, True)
time.sleep(2)

gpio.cleanup()

gpio.setmode(gpio.BOARD)

gpio.setup(12, gpio.OUT)
gpio.output(12, True)
time.sleep(2)


gpio.cleanup()
