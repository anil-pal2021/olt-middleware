from flask import Flask
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

cred = credentials.Certificate(
    "firebase_key.json"
)

firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')

def home():

    return {
        "status": "Broadband Digital OLT Server Running"
    }

@app.route('/sync')

def sync():

    onu = {

        "serial": "HWTC12345678",
        "ponPort": "1/1/1",
        "rxPower": "-24.5 dBm",
        "status": "online",
        "authorized": True,
    }

    db.collection("onus").document(
        onu["serial"]
    ).set(onu)

    return {
        "message": "ONU Synced Successfully"
    }

if __name__ == '__main__':

    app.run()