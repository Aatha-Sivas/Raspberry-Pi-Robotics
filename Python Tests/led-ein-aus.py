#!usr/bin/python3
#Beispieldatei led-ein-aus.py
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)

for i in range (10):
    gpio.output(7, gpio.HIGH)
    gpio.output(11, gpio.LOW)
    time.sleep(1)
    gpio.output(7, gpio.LOW)
    gpio.output(11, gpio.HIGH)
    time.sleep(1)



gpio.cleanup()
