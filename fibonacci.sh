#!/bin/bash
counter=0
first=0
second=1
temp=0
num=10
for (( i=0; i<$num; i++ ))
do
	echo "$first"
	temp=$(( first + second ))
	first=$second
        second=$temp	
done




