import firebase
import env
import result

db = firebase.Firebase()
db.authenticate(env.auth_cred)

print(db.get_poll_time("pi-1"))

# reading = result.Result(23, "Temperature")
# print(reading.date_time)