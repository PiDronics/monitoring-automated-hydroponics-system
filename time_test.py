import firebase
import env


db = firebase.Firebase()
db.authenticate(env.auth_cred)

db.push(7.1, "pH", "pi-1")



