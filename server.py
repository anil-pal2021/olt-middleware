from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():

    return {
        "status": "Broadband Digital OLT Server Running"
    }

@app.route('/sync')

def sync():

    return {
        "message": "ONU Sync Success"
    }

if __name__ == '__main__':
    app.run()