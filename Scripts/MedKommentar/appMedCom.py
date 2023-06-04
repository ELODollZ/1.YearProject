#!/usr/bin/env python3
# Author: NyboMønster
# Import libary list:
from flask import Flask, render_template        #importer 2 elementer/funktioner fra flask modulet komma bruges til at seperate
from flask_socketio import SocketIO, emit 
import time                                                       #normal import fra maskine (esp32 eller andet)
import threading
from BashInput import GetInputFromBash     #Import fra en lokal file på maskinen 

# Variables:
sensor = 25                                                          #Oprettes en variable med integer værdi 25
message = None                                                  #Oprettes en tom variable None er tom hvor imod 0 eller "zero" er stadig værdier
app = Flask(__name__)                                       #Flask funktionen til  at oprette hjemmesiden på en lokal host.
socketio = SocketIO(app)                                    #variablen sættes til en funktion fra SocketIO som skal sende til hjemmesiden.

# App route paths:
@socketio.on('hentTemp')                                   #flask's måde at finde filer eller andre funktioner på
def HentTemperatur():                                         #op rettes funktionen som henter vores data, og formater det til en str message og "emit" det til vores hjemmeside. under tagged "HentTemperatur"
    message = GetInputFromBash()
    print(message)
    message = str(message)
    time.sleep(0.5)
    socketio.emit('HentTemperatur', message)
@app.route('/')
def index():
    return render_template('Index.html')            #Index html side sættes her


# Main Code:
def readTemp():                                                 #Funktion til at læse temperaturen fra læsen
    global message
    while True:
        time.sleep(2)
        try:
            #message = sensor
            HentTemperatur()                                #Kalder funktion fra linje 18 som henter temperaturen (variablen opdaters i funktion så det behøver ikke at opdater igen)
            #print(message)
        except:
            message = None

tempThread = threading.Thread(target=readTemp)      #threaden oprettes, og angives den funktion med et while true loop som skal køre
tempThread.start()                                                          #Thread'en starts

# Host WebPage:
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)         #Websiden hosts, og den henter app variablen, og sætter vores host til 0.0.0.0
