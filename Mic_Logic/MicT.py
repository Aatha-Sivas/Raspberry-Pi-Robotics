#just some mic testing
#!/usr/bin/env python
import pyaudio
from numpy import zeros,linspace,short,fromstring,hstack,transpose,log
from scipy import fft
from time import sleep
from collections import deque
#import paho.mqtt.client as mqtt
import requests
import pygame.mixer
from pygame.mixer import Sound
import RPi.GPIO as GPIO

pygame.mixer.init(32000)
confirm = Sound("Music/OOT_Song_Correct.wav")

SENSITIVITY= 1.0

BANDWIDTH = 25

Ji = 310
Me = 420
Ha = 670
Do = 700

minHa = Ha-50
maxHa = Ha+BANDWIDTH
minJi = Ji-50
maxJi = Ji+BANDWIDTH
minMe = Me-50
maxMe = Me+BANDWIDTH
minDo = Do-50
maxDo = Do+BANDWIDTH

start = deque(['Ha','Ji','Me'])
notes = deque(['Do','Do','Do','Do','Do','Do'], maxlen=6)

frequencyoutput=True
freqNow = 1.0
freqPast = 1.0

devinfo = pa.get_device_info_by_index(1)  # Or whatever device you care about.
if pa.is_format_supported(44100.0,  # Sample rate
                         input_device=devinfo['index'],
                         input_channels=devinfo['maxInputChannels'],
                         input_format=pyaudio.paInt16):
  print ('Yay!')

NUM_SAMPLES = 2048
SAMPLING_RATE = 48000 #make sure this matches the sampling rate of your mic!
pa = pyaudio.PyAudio()
_stream = pa.open(format=pyaudio.paInt16,
                  channels=1, rate=SAMPLING_RATE,
                  input=True,
                  frames_per_buffer=NUM_SAMPLES)




while True:
    while _stream.get_read_available()< NUM_SAMPLES: sleep(0.01)
    audio_data  = fromstring(_stream.read(
        _stream.get_read_available()), dtype=short)[-NUM_SAMPLES:]
    # Each data point is a signed 16 bit number, so we can normalize by dividing 32*1024
    normalized_data = audio_data / 32768.0
    intensity = abs(fft(normalized_data))[:NUM_SAMPLES/2]
    frequencies = linspace(0.0, float(SAMPLING_RATE)/2, num=NUM_SAMPLES/2)
    if frequencyoutput:
        which = intensity[1:].argmax()+1
        # use quadratic interpolation around the max
        if which != len(intensity)-1:
            y0,y1,y2 = log(intensity[which-1:which+2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            # find the frequency and output it
            freqPast = freqNow
            freqNow = (which+x1)*SAMPLING_RATE/NUM_SAMPLES
        else:
            freqNow = which*SAMPLING_RATE/NUM_SAMPLES
    if minJi <= freqPast <= maxDo and abs(freqNow-freqPast) <= 25:
        if minHa<=freqPast<=maxHa and minHa<=freqNow<=maxHa and notes[-1]!='Ha':
            notes.append('Ha')
            print("You said Ha!")
        elif minJi<=freqPast<=maxJi and minJi<=freqNow<=maxJi and notes[-1]!='Ji':
            notes.append('Ji')
            print("You said Ji!")
        elif minMe<=freqPast<=maxMe and minMe<=freqNow<=maxMe and notes[-1]!='Me':
            notes.append('Me')
            print("You said Me!")
        elif minDo<=freqPast<=maxDo and minDo<=freqNow<=maxDo and notes[-1]!='Do':
            notes.append('Do')
            print("You said Do!")
        else:
            print("What the heck is that?")

    if notes==start:
        print("ITS MOVING BABY!!")
        confirm.play()
        notes.append('Do')
    
    








