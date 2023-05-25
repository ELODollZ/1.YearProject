#!/usr/bin/env python3
# Athur: NyboMønster
# Sources:
# Import list:
import sys
import random
import time
# Import fra onboardscripts:
from umqttsimple import MQTTClient
# Variables:
username = 'RPI/1YearProject'
password = 'RPIPass/1Year'
broker = 'broker.RPI.io'
msg = ("DeviceName:", "Temp", "Day")
Originmsg = ("DeviceName:", "Temp", "Day")


# Connection Function to RPI Broker
def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'1Year/ESP32Data' and msg == b'1Year/received':
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

# Startups
try:
    client = connect_and_subscribe()
    measuredData(Originmsg)
except OSError as e:
    restart_and_reconnect()
# Main Code:
while True:
    try:
        client.check_msg()
        if(time.time() - last_message) > message_interval:
            msg = measuredData(message)
            client.publish(topic, msg)
            last_message = time.time()
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

