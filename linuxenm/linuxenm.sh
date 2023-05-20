#!/usr/bin/bash
#This script is made by prince kumar
#date 17 may 2023
# Disclamer : this script is made for educational purpuses only i am not responsible for any illegal activity ..
# First get the uname information
echo -ne "\033[32;1m Machine : "
machine=$(uname -m)
echo -e "\033[33;1m $machine"
echo -ne "\033[32;1m Arc     : "
arc=$(uname -o)
echo -e "\033[33;1m $arc "
# Ask for the history cmd
echo -ne "\033[35;1m Press Y to see the history N to skip (default N): "
read history_optn
if [[ $history_optn == "Y" ]] || [[ $history_optn == "y" ]];then
        cd
        cat .bash_history

else
        echo ""

fi
echo -ne "\033[35;1m Press Y to see the all user N to skip it (default N): "
read user_optn
if [[ $user_optn == "Y" ]] || [[ $user_optn == "y" ]];then
        cat /etc/passwd | awk -F ":" '{ print $1 }'

else
        echo ""

fi
# now add the mote feture too this script...
