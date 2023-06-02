#!/usr/bin/env python3
# Author: NyboMønster

# Imports
import sys

# Variables
messages = ""
BashInput = "".join(sys.argv[1:])
# Main Code
def GetInputFromBash(BashInput):
    BashInput = "".join(sys.argv[1:])
    print(BashInput)
    for BashInput in sys.stdin:
        messages += [BashInput]
    BashInput = str(messages)
    print(BashInput)
    return BashInput
