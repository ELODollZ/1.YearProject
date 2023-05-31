#!/usr/bin/env python3
# Author: NyboMønster
# Sources:
# Import List:
import random
import time
#from TempSensor import tempReadSensor0
#from TempSensor1 import tempReadSensor1
#from TempSensor2 import tempReadSensor2
#from GetWeather9 import get_weather
# Variable List:
#TempDevice0 = tempReadSensor0()
#TempDevice1 = tempReadSensor1()
#TempDevice2 = tempReadSensor2()
message = ("DeviceNumber, Temp, Status")
DeviceList = ("ESP32 #1")
fullMessage = []
# initialized:
RandomNumberbool = random.randint(0,1)

def messageMaker(message, TempList, Status):
    for x in DeviceList:
        Swapped = "DeviceNumber," + DeviceList
        newmsg = message.replace("DeviceNumber", Swapped)
        Swapped = "Temp1, " + str(TempList[0]) + ", Temp2, " + str(TempList[1]) + ", Temp3, " + str(TempList[2])  
        newmsg = newmsg.replace("Temp", Swapped)
        Swapped = "Status, " + str(Status) + ", Fixed"
        newmsg = newmsg.replace("Status", Swapped)
    fullMessage.append(newmsg)
    newmsg = str(fullMessage)
    newmsg = newmsg.split(",", 11)
#    fullMessage.clear()
#    for x in newmsg:
#        Var1 = x.split(":", 4)
#        #print(Var1)
#        fullMessage.append(Var1)
    #newmsg = fullMessage
    return newmsg

# Main function Code:
def TempMeasure(msg):
    fullMessage.clear()
    #Temp0 = TempDevice0
    #temp1 = TempDevice1
    #Temp2 = TempDevice0
    Temp0 = random.randint(0, 100)
    Temp1 = random.randint(0, 100)
    Temp2 = random.randint(0, 100)
    if Temp1 - Temp2 >= 30:
        print("Vand Sluk 1")
        Status = False
    elif Temp1 - Temp2 <= 30:
        print("Vand Åben 2")
        Status = True
    else:
        print("Failure in sensor")
    # Message Update:
    TempList = Temp0, Temp1, Temp2
    newmsg = messageMaker(message, TempList, Status)
    #print(newmsg)
    return newmsg
#while True:
#    newmessage = TempMeasure(message)
#    print(newmessage)
#    time.sleep(1)
