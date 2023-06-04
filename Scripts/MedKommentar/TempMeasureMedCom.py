#!/usr/bin/env python3
# Author: NyboMønster
# Sources:
# Import List:
import random
import time
from machine import Pin
from TempSensor import tempReadSensor0                                  #Henter funktionen fra hvert af vores temperatur måler
from TempSensor1 import tempReadSensor1
from TempSensor2 import tempReadSensor2
#from GetWeather9 import get_weather
# Variable List:
message = ("DeviceNumber, Temp, Status")
DeviceList = ("ESP32 #1")
fullMessage = []
PinNumber = 0
VentileSwitch = Pin(PinNumber, Pin.OUT)
# initialized:
RandomNumberbool = random.randint(0,1)

def messageMaker(message, TempList, Status):                        #Funktionen der laver vores besked som skal sendes, og "erstatter" med de opsamlet værider, funktione kaldes først i linje 56 så "Status" er opdateret på dette tidspunkt
    for x in DeviceList:
        Swapped = "DeviceNumber," + DeviceList
        newmsg = message.replace("DeviceNumber", Swapped)
        Swapped = "Temp1, " + str(TempList[0]) + ", Temp2, " + str(TempList[1]) + ", Temp3, " + str(TempList[2])  
        newmsg = newmsg.replace("Temp", Swapped)
        GotTime = str(time.asctime())
        Swapped = "Status, " + str(Status)+ "," + GotTime + ", Fixed"
        newmsg = newmsg.replace("Status", Swapped)
    fullMessage.append(newmsg)
    newmsg = str(fullMessage)
    newmsg = newmsg.split(",", 11)                                          #splitter vores liste til 12 string elementer
    return newmsg

# Main function Code:
def TempMeasure(msg):                                                              #Funktion kaldt i main, som henter vores Temperatur, og returner den besked vi skal sende afsted til vores RPI,
    fullMessage.clear()                                                                  #Vi clear beskeden i tilfælde af det ikke er tid endnu til at sende beskeden (i main) og for ikke at ødelægge vores liste (start på en frisk hver gang)
    Temp0 = tempReadSensor0()
    Temp1 = tempReadSensor1()
    Temp2 = tempReadSensor2()
    #Temp0 = random.randint(0, 60)
    #Temp1 = random.randint(0, 60)
    #Temp2 = random.randint(0, 60)
    if Temp1 - Temp2 >= 30:
        print("Vand Sluk 1")
        Status = False
        VentileSwitch.off()
    elif Temp1 - Temp2 <= 30:
        print("Vand Åben 2")
        Status = True
        VentileSwitch.on()
    else:
        print("Failure in sensor")
    # Message Update:
    TempList = Temp0, Temp1, Temp2                                      #Laves en liste af hvad temperatur målingerne har målt
    newmsg = messageMaker(message, TempList, Status)           #Vores messageMaker som modtager 3 augmenter, beskeden den skal sende, temperatur værdierne, og status om den er åbnet eller lukket
    #print(newmsg)
    return newmsg                                                                           #Returner variablen fordi ellers får vi aldrig vores nye data ud af funktionen (data kommer aldrig ud af en funktion med mindre det er global eller med et return statement)
