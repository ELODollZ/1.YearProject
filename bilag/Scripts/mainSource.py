#! /bin/python3
### Author: NyboMønster
###Main File
### Imports fra system
import sys
import random
import time
### Imports fra costumscripts
from measure import measuredData, message
from umqttsimple import MQTTClient
import GPSScript
### Variables
username = 'RPI'
password = 'public'
broker = 'broker.RPI.io'
counter = 0
### KEA E bygning grønområde
msg = ("t, h, s, 55.69194647082459, 12.554169821375735")
Originmsg = ("t, h, s, 55.69194647082459, 12.554169821375735")
### Main Functions
def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'ESP32Data' and msg == b'received':
        print('ESP Sendt Data')

def connect_and_subscribe():
    global client_id, RPI_IP_Add, topic_pub, topic_sub, topic, port
    client = MQTTClient(client_id, RPI_IP_Add)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic)
    print('Connected to %s MQTT broker, subribed to %s topic' % (RPI_IP_Add, topic))
    return client
def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()
try:
### StartUps
    client = connect_and_subscribe()
    measuredData(Originmsg)
except OSError as e:
    restart_and_reconnect()
### Main Loop
while True:
    try:
        client.check_msg()
        if(time.time() - last_message) > message_interval:
            msg = measuredData(message)
            client.publish(topic, msg)
            last_message = time.time()
            counter += 1
            GPSScript.gpsFunktion1()
            time.sleep(0.5)
            print("------------------------------")
    except OSError as e:
        restart_and_reconnect()
    except TypeError:
        print("Type error somewhere in code, functional")
    except:
        print("STOP!")
        sys.exit
        time.sleep(2)