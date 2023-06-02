#!/bin/bash
# Author: NyboMønster

# Variables
message=""
IFS=','

# Main Code
while true
do
mosquitto_sub	-h	localhost	-t	"1Year/ESP32Data" -C	1	-R	"$messages" | while read -r messages
do
	echo "$messages"
	python app.py "$messages"
done
done
#
#Name0 Value0 Name1 Value1 Name2 Value2 Name3 Value3 Name4 Value4 Fixed;
#do
#	echo $Name0 $Value0 $Name1 $Value1 $Name2 $Value2 $Name3 $Value3 $Name4 $Value4 $Fixed
#	messages= $Name0, $Value0, $Name1, $Value1, $Name2, $Value2, $Name3, $Value3, $Name4, $Value4, $Fixed
#	echo $messages
