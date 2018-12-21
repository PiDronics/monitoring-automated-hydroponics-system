import pyrebase
import env
import time

# def get_historic(pi_id, sensorType):
    
#     return obj

# def calculate(sensorType, pi_id):
#     # Get Unix time for midnight today
#     values = []
#     time24hr = int(time.time()) - 86400
#     historic_data = get_historic(sensorType, pi_id)
#     for obj in historic_data:
#         if obj["time"] > time24hr:
#             values.append(obj["reading"])
#     # Values are added to a list, and from this list the min, max and avg are extrapolated
#     minVal = min(values)
#     maxVal = max(values)
#     avgVal = sum(values)/float(len(values))

#     print(minVal)
#     print(maxVal)
#     print(avgVal)

firebase = pyrebase.initialize_app(
            {
                "apiKey": env.auth_cred["API_KEY"],
                "authDomain": env.auth_cred["AUTH_DOMAIN"],
                "databaseURL": env.auth_cred["DATABASE_URL"],
                "storageBucket": env.auth_cred["STORAGE_BUCKET"]
            }
        )
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(env.auth_cred["EMAIL"], env.auth_cred["PASS"])
uid = user["localId"]

db.child("users").child(uid).child("systemData").child("PIDRONICS-TEST").child("sensors").child("pH").update({"avg":5.6, "current": 7.1, "max": 7.1, "min": 5.1}, user["idToken"])
# obj = db.child("users").child(uid).child("systemData").child("pi-1").child("sensorData").child("Temperature").get().val()
# calculate("Temperature", "pi-1")
# print(obj)