#!/bin/bash

# desc: monitoring services



# checking for serivice name as an argument
if [ $# -eq 0 ];
then
	echo "Usage: $(basename $0) [service name]."
fi

# checking the installation of the service
service=$(which $1|cut -d/ -f5)

if [ $? -ne 0 ] || [ -z $service ]; then
	echo "$service not found... exiting"
	exit
fi

echo "checking for $service"

#checking for pid
while [ 1 ]
do 
	echo "checking $service"
	ps -e | grep $service &>/dev/null
	#checking if the service is stopped
	if [ $? -ne 0 ]; then
		echo "$service stopped .... restarting"
		i=0
		while [ $i -lt 3 ]
		do 
			systemctl start $service
		 	[ $? -eq 0 ] && break
			i=$((i + 1))
			sleep 1
		done
	fi 
	sleep 3
done

#notify the admin if the service couldn't be restarted

echo "Service $service couldn't be restarted" | mail -s "$service stopped" root


