#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
messages = ""
BashInput = ""
# Main Code
def GetInputFromBash(BashInput):
    print(BashInput)
    for BashInput in sys.stdin:
        messages += [BashInput]
    BashInput = str(messages)
    print(BashInput)
    return BashInput
