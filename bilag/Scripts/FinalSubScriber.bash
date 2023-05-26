#!/bin/bash
# Author: NyboMønster

# Variables
messages=""
SentMessages="Messages sent"
IFS=','

# Main Code
while true
do
mosquitto_sub	-h	localhost	-t	"1Year/ESP32Data" -C	1	-R	$messages | while true
do 
	echo $messages
	sleep 1
done
done

