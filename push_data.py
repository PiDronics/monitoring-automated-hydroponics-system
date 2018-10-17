import pyrebase
import env
from poll_sensors import poll

firebase = pyrebase.initialize_app(
    {
        "apiKey": env.API_KEY,
        "authDomain": env.AUTH_DOMAIN,
        "databaseURL": env.DATABASE_URL,
        "storageBucket": env.STORAGE_BUCKET
    }
)
db = firebase.database()
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(env.EMAIL, env.PASS)

while True:
    result = poll()
    db.child("systems").child("pi-1").child("data-dev").push(result, user["idToken"])
    
