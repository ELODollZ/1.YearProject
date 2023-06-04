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
def sub_cb(topic, msg):                                 # funktionen bruges til at "tømme" skraldet i ens forbindelse, den tjekker også om vores forbindelse har modtaget vores besked
    print((topic, msg))
    if topic == b'ESP32Data' and msg == b'received':
        print('ESP Sendt Data')

def connect_and_subscribe():                        # Funtkionen til at oprette forbindelse til vores RPI og "Topic" den samtale vores maskiner taler over
    global client_id, RPI_IP_Add, topic_pub, topic_sub, topic, port
    client = MQTTClient(client_id, RPI_IP_Add)
    client.set_callback(sub_cb)                         # funktioner kaldes fra MQTT importet, se "umqttsimple.py"
    client.connect()
    client.subscribe(topic)
    print('Connected to %s MQTT broker, subribed to %s topic' % (RPI_IP_Add, topic))
    return client                                                  # retuner client varaiblen ud af funktionen, at der er oprette forbindelse
def restart_and_reconnect():                            # Funktionen til at restart forbindelsen, den kan "refresher" efter 10 sekunder, hint de 10 sekunder sleep timer
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)

# Startups
try:                                                                        #Try Except til at connecte til vores RPI når den skal starte op.
    client = connect_and_subscribe()
    TempMeasure(Originmsg)
except OSError as e:
    restart_and_reconnect()
# Main Code:
while True:                                                                                  #hoved loopet der kører på vores ESP32
    try:
        client.check_msg()
        if(time.time() - last_message) > message_interval:          #If statement der tjekker om det er tid til at sende en ny besked.
            msg = TempMeasure(msg)                                            #henter vores besked fra vores data måler, som skal sendes
            msg = str(msg)
            client.publish(topic, msg)                                              #sendes af sted til vores topic
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

