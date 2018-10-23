import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)

def poll():
  try:
    result = instance.read()
  except AttributeError:
    print("Method does not exist")
    if result.is_valid():
        return {
          "TimeStamp": int(time.time()), 
          "Temperature: C": result.temperature, 
          "Temperature: F": ((result.temperature * 9/5) + 32),
          "Humidity": result.humidity
        }
