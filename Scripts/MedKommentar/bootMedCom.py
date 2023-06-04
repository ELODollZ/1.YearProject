#! /bin/python3
###Author: NyboMønster
### Imports fra ESP'en selv
import esp
esp.osdebug(None)
#import webrepl
#webrepl.start()
import network
import time
import ubinascii
import machine
import micropython
import gc
import random
gc.collect()
### Imports fra scripts
from umqttsimple import MQTTClient              #Importet som skal bruges til at sendes med over internettet og MQTT protocollen
##Variables:
cooldownTimer = 5
last_message = 0
counter = 0
message_interval = 10
### Credits:                                                        #Listen af variabler som bruges til at config RPI og MQTT protocollen
ssid = 'Gruppe9PI'
password = 'Gruppe9PI'
RPI_IP_Add = '192.168.53.56'
ESP32_IP_Add = '192.168.239.88'
port = 1883
client_id = f'python-mqtt-{0807}'
topic = "1Year/ESP32Data"

### MainCode
station = network.WLAN(network.STA_IF)                  #variablen oprettes

station.active(True)
station.connect(ssid, password)                                     #Opretter forbindelse til internettet, (eller netværket mere korrekt)

while station.isconnected() == False:
    pass
print('Connection succesful')
print(station.ifconfig())
