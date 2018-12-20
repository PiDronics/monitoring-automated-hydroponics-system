import pyrebase
from time import sleep, time
import datetime
import result

class Firebase:
    
    def __init__(self):
        pass

    def authenticate(self, auth_cred):
        self.firebase = pyrebase.initialize_app(
            {
                "apiKey": auth_cred["API_KEY"],
                "authDomain": auth_cred["AUTH_DOMAIN"],
                "databaseURL": auth_cred["DATABASE_URL"],
                "storageBucket": auth_cred["STORAGE_BUCKET"]
            }
        )
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password(auth_cred["EMAIL"], auth_cred["PASS"])
        self.uid = self.user["localId"]

    def get_poll_time(self, pi_id):
        obj = self.db.child("systems").child(pi_id).child(self.uid).get().val()
        return (float(obj["interval"]) * 60)
    
    def push(self, value, sensor, pi_id):

        reading = result.Result(value, sensor)

        # Pushing value as current
        self.db.child("users").child(self.uid).child("systemCard").child(pi_id).child("sensors").child(sensor).update({"current":value, "enabled":"true", "status": reading.status})
        #Updating last update date and time
        self.db.child("users").child(self.uid).child("systemCard").child(pi_id).update({"lastUpdated":reading.date_time})
        
        # Pushing to historic
        self.db.child("users").child(self.uid).child("systemData").child(pi_id).child("sensorData").child(sensor).child("allData").push({"reading":26, "time": reading.unix_time})
        # Updating last updated time
        self.db.child("users").child(self.uid).child("systemData").child(pi_id).update({"lastUpdated":reading.date_time})