import RPi.GPIO as GPIO
import ph
import temp
import time
import datetime
import env
import firebase

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

tempSensor = temp.TemperatureSensor()
phSensor = ph.I2CSensor(99) # 99 or 63 (hexadecimal) represents the pH sensor.
                          # Theoretically, this code can work for many i2c probes such as EC and DO by simply changing this parameter.

db = firebase.Firebase()
db = db.authenticate(env.auth_cred)


while True:  # Repeat the code indefinitely

  time.sleep(300)  # read sensor circuit every 300 sec (5 min)

  # pH Sensor
  try:
      ph_reading = phSensor.query("R")
      print (ph_reading)
      try:
        db.push(ph_reading, "pH")
      except:
        print("Error pushing to database")

  except IOError:
      print ("Query failed")

  try:
    temp_reading = tempSensor.read()
    if temp_reading.is_valid():
      
      print("Temperature: %d C" % temp_reading.temperature)
      print("Humidity: %d %%" % temp_reading.humidity)

      db.push(temp_reading.temperature, "Temperature")
      db.push(temp_reading.humidity, "Humidity")
  except IOError:
    print ("Query failed")