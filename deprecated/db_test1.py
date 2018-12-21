import firebase
import env

db = firebase.Firebase()
db.authenticate(env.auth_cred)

db.push(6.8, "pH", "pi-1")

db.push(6.8, "pH", "pi-1")
db.push(6.5, "pH", "pi-1")
db.push(6.2, "pH", "pi-1")
db.push(4.3, "pH", "pi-1")
db.push(7.1, "pH", "pi-1")