from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/devices')
def devices():
    devices = os.popen("arp -a").read()
    return devices

if __name__ == '__main__':
    app.run()
