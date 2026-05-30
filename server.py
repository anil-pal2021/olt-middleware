from flask import Flask
import firebase_admin
import os
import json

from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

firebase_json = os.environ.get("FIREBASE_KEY")

firebase_dict = json.loads(firebase_json)

cred = credentials.Certificate(firebase_dict)

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
        "txPower": "2.1 dBm",
        "status": "online",
        "oltId": "OLT001"
    }

    db.collection("onus").add(onu)

    return {
        "message": "ONU Synced Successfully"
    }

if __name__ == '__main__':

    app.run()