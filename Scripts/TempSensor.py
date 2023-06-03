#!/usr/bin/env python3
# Author: NyboMønster
# Sources:
# Imports list:
from machine import Pin, ADC
import time

# Variable list:
PinNumber = 32
tempSensor = ADC(Pin(PinNumber))
tempSensor.atten(ADC.ATTN_0DB)
# Config Information value calculation
ADCOffset = 2.1
MiniADC = 0
MaxADC = 4095
MaxVoltage = 0.950
mV = 0.010
# Main function code:

def tempReadSensor1():
    #print(1)
    value = tempSensor.read()
    #Test1 = (MaxADC / )
    voltage = ((value / MaxADC) * MaxVoltage)
    CelciusValue = (((value / MaxADC) * MaxVoltage) / mV) + ADCOffset
    print(value)
    print(CelciusValue)
    return CelciusValue
#while True:
#    tempReadSensor()
#    time.sleep(1)
