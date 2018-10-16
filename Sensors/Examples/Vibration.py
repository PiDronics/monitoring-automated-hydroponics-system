#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

channel = 17
GPIO.setmode(GPIO.BCM)       
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
            print "Movement Detected!"
        else:
            print "Movement Detected!"

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) #let is know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback) # assign function to GPIO PIN, Run function on change

while True:
    time.sleep(1)
