#!/usr/bin/env python3
# Athur: NyboMønster
# Sources:
# Import list:
import sys
import random
import time
from TempMeasure import TempMeasure
# Import fra onboardscripts:
from umqttsimple import MQTTClient
# Variables:
username = '1YearProject'
password = 'public'
broker = 'broker.RPI.io'
msg = ("DeviceName:", "Temp:", "Status:")
Originmsg = ("DeviceName:", "Temp:", "Status:")


# Connection Function to RPI Broker
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

# Startups
try:
    client = connect_and_subscribe()
    TempMeasure(Originmsg)
except OSError as e:
    restart_and_reconnect()
# Main Code:
while True:
    try:
        client.check_msg()
        if(time.time() - last_message) > message_interval:
            msg = TempMeasure(msg)
            msg = str(msg)
            client.publish(topic, msg)
            last_message = time.time()
            time.sleep(0.5)
            print("------------------------------")
    except OSError as e:
        restart_and_reconnect()
#    except TypeError:
#        print("Type error somewhere in code, functional")
    except:
        print("STOP!")
        sys.exit
        time.sleep(2)

