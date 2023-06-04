#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
BashInput = ""

# Main Code
def GetInputFromBash():
    var1 = sys.argv[1]                      #sys tillader at modtage information fra andre filer end python, her angives augment 1 fordi data'en fra vores MQTT protocol bliver sendt over mosquittto, og vi fra valgte flask løsning om at modtage information
    print(var1)
    BashInput = var1.split(";")         #splitter vores data list ved ;
    print(BashInput)
    return BashInput
#BashInput = GetInputFromBash()
#print(BashInput)

