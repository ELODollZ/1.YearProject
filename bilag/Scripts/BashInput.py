#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
messages = ""
BashInput = ""
# Main Code
def GetInputFromBash(BashInput):
    BashInput.clear()
    for BashInput in sys.stdin:
        messages += [BashInput]
    BashInput = messages
    print(BashInput)
    return BashInput
