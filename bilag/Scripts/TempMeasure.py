#!/usr/bin/env python3
# Author: NyboMønster
# Sources:
# Import List:
#from machine import Pin
import random
#import dht
import time

# Variable List:
TempDevice0 = 0#dht.DHT11(Pin(25))
TempDevice1 = 1#dht.DHT11(Pin(26))
TempDevice2 = 2#dht.DHT11(Pin(27))
message = ("DeviceNumber: , Temp:, Status:")
DeviceList = ("ESP32 #1")
fullMessage = []
# initialized:
RandomNumberbool = random.randint(0,1)

def messageMaker(message, TempList, Status):
    for x in DeviceList:
        Swapped = "DeviceNumber: " + DeviceList
        newmsg = message.replace("DeviceNumber: ", Swapped)
        Swapped = "Temp: " + str(TempList[0]) + ", Temp: " + str(TempList[1]) + ", Temp: " + str(TempList[2])  
        newmsg = newmsg.replace("Temp", Swapped)
        Swapped = "Status: " + str(Status)
        newmsg = newmsg.replace("Status:", Swapped)
    fullMessage.append(newmsg)
    newmsg = fullMessage
    return newmsg

# Main function Code:
def TempMeasure(msg):
    fullMessage.clear()
    #Temp0 = TempDevice0.temperature()
    #temp1 = TempDevice1.temperature()
    #Temp2 = TempDevice2.temperature()
    Temp0 = random.randint(0, 100)
    Temp1 = random.randint(0, 100)
    Temp2 = random.randint(0, 100)
    if Temp1 >= 40 or Temp1 >= 30:
        print("Vand Sluk 1")
        Status = False
    elif Temp1 <= 40 or Temp1 <= 30:
        print("Vand Åben 2")
        Status = True
    else:
        print("Failure in sensor")
    # Message Update:
    TempList = Temp0, Temp1, Temp2
    newmsg = messageMaker(message, TempList, Status)
    return newmsg
while True:
    newmessage = TempMeasure(message)
    print(newmessage)
    time.sleep(1)
