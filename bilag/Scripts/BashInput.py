#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
message = ""
BashInput = ""
# Main Code
def GetInputFromBash(BashInput):
    BashInput.clear()
    for message in sys.stdin:
        BashInput += [message]
    print(BashInput)
    return BashInput
