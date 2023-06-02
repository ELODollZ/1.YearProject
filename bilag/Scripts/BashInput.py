#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
messages = ""
BashInput = "".join(sys.argv[1:])
# Main Code
def GetInputFromBash(BashInput):
    var1 = sys.argv[1]
    print(BashInput) 
    BashInput = var1.split(";")
    print(BashInput)
    return BashInput
