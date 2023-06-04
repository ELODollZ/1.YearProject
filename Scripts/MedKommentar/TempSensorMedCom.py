#!/usr/bin/env python3
# Author: NyboMønster
# Sources:
# Imports list:
from machine import Pin, ADC
import time

# Variable list:
PinNumber = 32                          # Konfig på Temperatur måleren
tempSensor = ADC(Pin(PinNumber))
tempSensor.atten(ADC.ATTN_0DB)
# Config Information value calculation
ADCOffset = 2.1
MiniADC = 0
MaxADC = 4095
MaxVoltage = 0.950
mV = 0.010
# Main function code:

def tempReadSensor0():                                                  #Funktionen som vores Tempmeasure kalder, for at henter temperatur målingen.
    #print(1)
    value = tempSensor.read()
    #Test1 = (MaxADC / )
    voltage = ((value / MaxADC) * MaxVoltage)
    CelciusValue = (((value / MaxADC) * MaxVoltage) / mV) + ADCOffset               #Formlen: "Value / Den højest muligt ADC måling * Den Højest spænding (findes i datasheet) / med milivolten, evt sætter man et offsæt siden, hver sensor kan være forskellige og måle slightly off"
    print(value)
    print(CelciusValue)
    return CelciusValue                                                                                                     #Returner vores Celcius ud af vores funktion.
