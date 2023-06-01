#!/bin/bash
# Author: NyboMønster

# Variables
messages=""
SentMessages="Messages sent"
IFS=','

# Main Code
while true
do
mosquitto_sub	-h	localhost	-t	"1Year/ESP32Data" -C	1	-R	$messages
python app.py "$messages"
echo $messages
sleep 1
done
