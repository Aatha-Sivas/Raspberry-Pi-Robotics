#usr!/bin/python
#Joystick-Test joystick-ic2.py

from Adafruit_ADS1x15 import ADS1x15
from time import sleep

import time, signal, sys, os
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

delayTime = 2 #in Sekunden

# assigning the ADS1x15 ADC

ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit

# choosing the amplifing gain
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V

# choosing the sampling rate
# sps = 8    # 8 Samples per second
# sps = 16   # 16 Samples per second
# sps = 32   # 32 Samples per second
sps = 64   # 64 Samples per second
# sps = 128  # 128 Samples per second
# sps = 250  # 250 Samples per second
# sps = 475  # 475 Samples per second
# sps = 860  # 860 Samples per second

# assigning the ADC-Channel (1-4)
adc_channel_0 = 0    # Channel 0
adc_channel_1 = 1    # Channel 1
adc_channel_2 = 2    # Channel 2
#adc_channel_3 = 3    # Channel 3 #is not needed.

# initialise ADC (ADS1115)
adc = ADS1x15(ic=ADS1115)
################################################################################

#Main

try:
        while True:
                #read values
                adc0 = adc.readADCSingleEnded(adc_channel_0, gain, sps)
                adc1 = adc.readADCSingleEnded(adc_channel_1, gain, sps)
                adc2 = adc.readADCSingleEnded(adc_channel_2, gain, sps)
                #adc3 = adc.readADCSingleEnded(adc_channel_3, gain, sps)

                #print to console
                print ("--------------------------------------------")
                print("X : {}  Y : {}  Switch : {}".format(adc0,adc1,adc2))

                time.sleep(delayTime)



except KeyboardInterrupt:
        gpio.cleanup()
                

            

