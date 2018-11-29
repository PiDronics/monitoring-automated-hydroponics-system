# Test if libraries are imported
try:
  import RPi.GPIO as GPIO
except ImportError:
  print("Could not load raspberry pi library.")

try:
  import dht11
except ImportError:
  print("Could not load dht11 temperature/humidity sensor library")

import time
import datetime

# initialize GPIO and test if methods exist
try:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.cleanup()
except:
  print("GPIO method does not exist.")

# read data using pin 17
try:
  instance = dht11.DHT11(pin=17)
except:
  print("DHT11 Method does not exist.")

def poll():
  # Test if the library method read() exists
  try:
    result = instance.read()
  except AttributeError:
    print("DHT11 Method, read() does not exist.")

  try:
    if result.is_valid():
        return {
          "TimeStamp": int(time.time()), 
          "Temperature: C": result.temperature, 
          "Temperature: F": ((result.temperature * 9/5) + 32),
          "Humidity": result.humidity
        }
  except:
    print("Function did not return")