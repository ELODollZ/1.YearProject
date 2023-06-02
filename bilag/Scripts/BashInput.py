#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
BashInput = ""

# Main Code
def GetInputFromBash():
    var1 = sys.argv[1]
    print(var1)
    BashInput = var1.split(";")
    print(BashInput)
    return BashInput
#BashInput = GetInputFromBash()
#print(BashInput)

