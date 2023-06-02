#!/usr/bin/env python3
# Author: NyboMønster
# Import libary list:
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading
from BashInput import GetInputFromBash, messages

# Variables:
sensor = 25
message = None
app = Flask(__name__)
socketio = SocketIO(app)

# App route paths:
@socketio.on('hentTemp')
def HentTemperatur():
    message = GetInputFromBash(messages)
    message = str(message)
    time.sleep(0.5)
    socketio.emit('HentTemperatur', message)
@app.route('/')
def index():
    return render_template('Index.html')


# Main Code:
def readTemp():
    global message
    while True:
        time.sleep(2)
        try:
            #message = sensor.read()
            #message = sensor
            HentTemperatur()
            #print(message)
        except:
            message = None

tempThread = threading.Thread(target=readTemp)
tempThread.start()

# Host WebPage:
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
