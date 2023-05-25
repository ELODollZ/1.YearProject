#!/bin/bash
#Author: NyboMønster
###Variables
messages=""
#pastmessages=""
#testmessages="123.4, 123.4, False, 123.4, 123.4"
SentMessages="Messages sent"
DataBase="/home/NyboMønster/IOT2-Projekt/RPI/measuredData.db"
IFS=','
###Main Code
while :
do
mosquitto_sub	-h	localhost	-t	"ESP32Data" -C	1	-R	$messages | while read TEMP HUMD SMOKE XLOCATION YLOCATION; do
	echo $TEMP $HUMD $SMOKE $XLOCATION $YLOCATION
	sqlite3 $DataBase "INSERT INTO measuredData(TEMP,HUMD,SMOKE,XLOCATION,YLOCATION) VALUES ($TEMP,$HUMD,$SMOKE,$XLOCATION,$YLOCATION);"
	echo $SentMessages
done
done

