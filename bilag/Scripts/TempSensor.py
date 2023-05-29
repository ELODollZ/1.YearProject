#!/usr/bin/env python3
# Author: NyboMønster
# Sources:
# Imports list:
from machine import Pin, ADC
import time

# Variable list:
PinNumber = 25
tempSensor = ADC(Pin(PinNumber))
tempSensor.atten(ADC.ATTN_0DB)
tempSensor.width(ADC.WIDTH_12BIT)
Minimum = 0
Maximum = 4096

# Main function code:

def tempReadSensor():
    value = tempSensor.read()
    CelciusValue = value - 500 / 10
    print(value)
    print(CelciusValue)
    return CelciusValue
