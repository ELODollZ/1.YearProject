#!/bin/bash
#Author: NyboMønster
# Variables
messages=""
#testmessages="123.4, 123.4, False, 123.4, 123.4"
SentMessages="Messages sent"
IFS=','
###Main Code
while :
do
mosquitto_sub	-h	localhost	-t	"1Year/ESP32Data" -C	1	-R	$messages 
done

