#!/usr/bin/env python3
# Author: NyboMønster
# Import libary list:
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

# Variables:
sensor = None
sidsteTemp = None
app = Flask(__name__)
socketio = SocketIO(app)

# App route paths:
#@socketio.on('hentTemp')
#def hentTemp():
#    time.sleep(0.5)
#    socketio.emit('temp', sidsteTemp)
@app.route('/')
def index():
    return render_template('Index.html')


# Main Code:
#def readTemp():
#    global sidsteTemp
#    while True:
#        time.sleep(2)
#        try:
#            sidsteTemp = sensor.read()
#        except:
#            sidsteTemp = None
#
#tempThread = threading.Thread(target=readTemp)
#tempThread.start()


# Host WebPage:
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
