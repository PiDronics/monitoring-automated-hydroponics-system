import RPi.GPIO as GPIO
import i2c
import temp
import time
import datetime
import env
import firebase

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

tempSensor = temp.TemperatureSensor()
phSensor = i2c.I2CSensor(99) # 99 or 63 (hexadecimal) represents the pH sensor.
                            # Theoretically, this code can work for many i2c probes such as EC and DO by simply changing this parameter.

db = firebase.Firebase()
db.authenticate(env.auth_cred)
pi_id = env.auth_cred["PI_ID"]
poll_time = db.get_poll_time(pi_id)

while True:  # Repeat the code indefinitely

  # read poll time from database
  poll_time = db.get_poll_time(pi_id)
  time.sleep(poll_time)

  # pH Sensor
  try:
      ph_reading = phSensor.query("R")
      print (ph_reading)
      try:
        db.push(ph_reading, "pH", pi_id)
      except:
        print("Error pushing to database")

  except IOError:
      print ("Query failed")

  try:
    temp_reading = tempSensor.read()
    if temp_reading.is_valid():
      
      print("Temperature: %d C" % temp_reading.temperature)
      print("Humidity: %d %%" % temp_reading.humidity)

      db.push(temp_reading.temperature, "Temperature", pi_id)
      db.push(temp_reading.humidity, "Humidity", pi_id)
  except IOError:
    print ("Query failed")
