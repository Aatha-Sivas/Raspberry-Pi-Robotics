#usr!/bin/python
#Rover Movement with Joystick robo-stick.py

from Adafruit_ADS1x15 import ADS1x15
from time import sleep

import time, signal, sys, os, math
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

##################################################################################
###### Joystick-Config I2C BUS 

delayTime = 1

# assigning the ADS1x15 ADC

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit

# choosing the amplifing gain
gain = 4096  # +/- 4.096V

# choosing the sampling rate
sps = 64   # 64 Samples per second

# assigning the ADC-Channel (1-4)
adc_channel_0 = 0    # Channel 0
adc_channel_1 = 1    # Channel 1
adc_channel_2 = 2    # Channel 2

# initialise ADC (ADS1115)
adc = ADS1x15(ic=ADS1115)


######################################################################################3
    #######################################################################
        # Rover Movement

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(29, gpio.OUT)
    gpio.setup(31, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    
def forward():
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
    #time.sleep(tf)
    gpio.cleanup()

def backward():
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(7, True)
    #time.sleep(tf)
    gpio.cleanup()
    
def turnright():
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(29, False)
    gpio.output(31, True)
    gpio.output(7, True)
    #time.sleep(tf)
    gpio.cleanup()

def turnleft():
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(29, True)
    gpio.output(31, False)
    gpio.output(7, True)
    #time.sleep(tf)
    gpio.cleanup()

def stop():
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(29, False)
    gpio.output(31, False)
    gpio.output(7, False)
    #time.sleep(tf)
    gpio.cleanup()
    
################################################################################
    ######################################################################

    # Main

try:
        while True:
                #read values
                adc0 = adc.readADCSingleEnded(adc_channel_0, gain, sps)
                adc1 = adc.readADCSingleEnded(adc_channel_1, gain, sps)
                adc2 = adc.readADCSingleEnded(adc_channel_2, gain, sps)

                if (adc1 < 4):
                    #Forward
                    init()
                    gpio.output(13, True)
                    gpio.output(15, False)
                    gpio.output(29, True)
                    gpio.output(31, False)
                    gpio.output(7, True)
                    #time.sleep(tf)
                    
                if (adc1 > 3000):
                    #Backward
                    init()
                    gpio.output(13, False)
                    gpio.output(15, True)
                    gpio.output(29, False)
                    gpio.output(31, True)
                    gpio.output(7, True)
                    #time.sleep(tf)
                    
                if (adc1 > 1613 and adc1 < 1615):
                    #STOP
                    init()
                    gpio.output(13, False)
                    gpio.output(15, False)
                    gpio.output(29, False)
                    gpio.output(31, False)
                    gpio.output(7, False)
                    #time.sleep(tf)
                    
                if (adc0 > 3000):
                    #Turn Right
                    init()
                    gpio.output(13, True)
                    gpio.output(15, False)
                    gpio.output(29, False)
                    gpio.output(31, True)
                    gpio.output(7, True)
                    #time.sleep(tf)
                    
                if (adc0 < 4):
                    #Turn Left
                    init()
                    gpio.output(13, False)
                    gpio.output(15, True)
                    gpio.output(29, True)
                    gpio.output(31, False)
                    gpio.output(7, True)
                    #time.sleep(tf)
                    
                if (adc2 < 1):
                    gpio.cleanup()
                    sys.exit()

                #print ("--------------------------------------------")
                #print("X : {}  Y : {}  Switch : {}".format(adc0,adc1,adc2))

                #time.sleep(delayTime)

except KeyboardInterrupt:
        gpio.cleanup()
