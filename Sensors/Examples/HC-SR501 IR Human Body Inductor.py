import RPi.GPIO as GPIO                           #Import GPIO library
import time                                       #Import time library
GPIO.setmode(GPIO.BCM)                          #Set GPIO pin numbering
pir = 21                                    #Associate pin 26 to pir
GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO in 
print "Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate

try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"

    while True:
        if GPIO.input(pir):                            #Check whether pir is HIGH
            print "Motion Detected!"
        time.sleep(1)                               #D1- Delay to avoid multiple detection

except KeyboardInterrupt:
    print " Quit "
    GPIO.cleanup()
