#!usr/bin/python3
#1.Test Motodriver-GPIO.py
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(29, gpio.OUT)
gpio.setup(31, gpio.OUT)



gpio.output(13, True)
#gpio.output(15, gpio.HIGH)
#time.sleep(1)
gpio.output(29, True)
time.sleep(1)
#gpio.output(31, gpio.LOW)
#time.sleep(5)

gpio.cleanup()

print("Task over")
























    
