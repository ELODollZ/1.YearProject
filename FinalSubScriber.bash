#!/usr/bin/env bash
# Author: NyboMønster

# Variables
messages=""

# Main Code
while true
do
mosquitto_sub   -h      localhost       -t      "1Year/ESP32Data" -C    1       -R      $messages | while read messages
do      
        messages=$(printf "%s;" "$messages")
        echo $messages
        python3 BashInput.py "$messages"
done
done
