import pyrebase
from time import sleep, time

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
    
    def push(self, value, sensor):
        # Pushing value as current
        self.db.child("users").child("user1").child("systemCard").child("pi-1").child("sensors").child(sensor).child("current").push(value, self.user["idToken"])

        # Pushing value to historic
        self.db.child("users").child("user1").child("systemData").child("pi-1").child("sensorData").child(sensor).child("allData").push({value, int(time())}, self.user["idToken"])