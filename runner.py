import datetime
import time

import env
import firebase
import i2c

phSensor = i2c.I2CSensor(99) # 99 or 63 (hexadecimal) represents the pH sensor.
                             # Theoretically, this code can work for many i2c probes such as EC and DO by simply changing this parameter.

db = firebase.Firebase()
db.authenticate(env.auth_cred)
pi_id = env.auth_cred["PI_ID"]
poll_time = db.get_poll_time(pi_id)

while True:  # Repeat the code indefinitely

  # pH Sensor
  ph_reading = phSensor.query("R")
  print (ph_reading)
  db.push(ph_reading, "pH", pi_id)
  print("Push successful!")

  # read poll time from database
  poll_time = db.get_poll_time(pi_id)
  print(poll_time)
  time.sleep(poll_time)
