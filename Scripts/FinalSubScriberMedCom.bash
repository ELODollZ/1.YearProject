#!/usr/bin/env bash
# Author: NyboMønster

# Variables
messages=""                                  #Vores tomme liste

# Main Code
while true                                      #Vores true loop i bash
do
# Mosquitto_sub er en kommando, -h for at fortælle den skal bruge et augment, localhost, -t er topic, -C er counteren, antallet af gang det skal køre, -R for at læse message,
mosquitto_sub   -h      localhost       -t      "1Year/ESP32Data" -C    1       -R      $messages | while read messages                         #Vi køre 2 true loopes, så længe mosquitto ikke køre, sendes data, eller lytter den på vores topic
do                                                                                                                      # Do  bruges til at vise man er færdig med at augmenter for et loop,
        messages=$(printf "%s;" "$messages")
        echo $messages
        python3 BashInput.py "$messages"                                                        #kommandoen som passer vores variable til python kode, som en string 
done
done                                                                                                                    # Done giver sig selv, den er færdig med loopet
