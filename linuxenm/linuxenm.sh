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
#Which program is installed to download remote file check wget,nc,natcat
check_prog_down(){
        command -v wget 2>&1 > /dev/null && echo -e "\033[0;1m Wget is installed " || { echo -e "\033[32;1m Wget is not installed" ; }
        command -v natcat 2>&1 /dev/null && echo -e "\033[0;1m natcat is installed" || { echo -e "\033[32;1m natcat is not installed ";}
}
check_prog_down
# check services running as root
service_as_root(){
echo -e "\033[34;1m These services are runnig as root"
ps aux | grep "root"
}
service_as_root
