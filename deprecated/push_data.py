import pyrebase
from time import sleep

try:
    from env import API_KEY, 
                    AUTH_DOMAIN, 
                    DATABASE_URL, 
                    STORAGE_BUCKET, 
                    EMAIL, 
                    PASS
except ImportError:
    print("No .env file found.\mCould not load Firebase Credentials.")

try:
    from poll_sensors import poll
except ImportError:
    print("Could not load sensor library.")

try:
    from rpi_command import restart
except ImportError:
    print("Could not load Raspberry Pi commands.")


firebase = pyrebase.initialize_app(
    {
        "apiKey": API_KEY,
        "authDomain": AUTH_DOMAIN,
        "databaseURL": DATABASE_URL,
        "storageBucket": STORAGE_BUCKET
    }
)
db = firebase.database()
auth = firebase.auth()

user = auth.sign_in_with_email_and_password(EMAIL, PASS)

while True:
    result = poll()

    db.child("users").child("user1").child("systemCard").child("pi-1").child("sensors").child("Temperature").child("current").push(result["Temperature: C"], user["idToken"])
    db.child("users").child("user1").child("systemData").child("pi-1").child("sensorData").child("Temperature").child("allData").push(result, user["idToken"])
    sleep(300) # Polls and pushes every 5m to reduce overhead
    
    # Commands Raspberry Pi to restart if user/administrator finds fault
    # Database push is made and flag field is changed. Value is read and restart
    # command is initiated.
    
    # Read triggerRestart flag field
    restart_flag = db.child("users").child("user1").child("systemCard").child("pi-1").child("commands").child("triggerRestart")

    if restart_flag:
        # Reset triggerRestart flag field back to 0
        db.child("users").child("user1").child("systemCard").child("pi-1").child("commands").child("triggerRestart").push(0, user["idToken"])
        
        restart()
        # Nothing is reachable after this function (obviously)
