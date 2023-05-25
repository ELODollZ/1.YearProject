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
message = ("DeviceNumber, Temp, Status")
message.split(", ", 2)
DeviceList = ("DeviceNumber0", "DeviceNumber1", "DeviceNumber2")
TempList = ("Temp0", "Temp1", "Temp2")
# initialized:
RandomNumberbool = random.randint(0,1)

# Main function Code:
def TempMeasure(Input, Output):
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
    for x in DeviceList:
        Swapped = "DeviceNumber:" + x
        newmsg = message.replace("DeviceNumber", Swapped)
        Swapped = str(TempList)
        newmsg = newmsg.replace("Temp", Swapped)
        Swapped = str(Status)
        newmsg = newmsg.replace("Status", Swapped)
        print(newmsg)
while True:
    TempMeasure(TempDevice0, None)
    time.sleep(1)
