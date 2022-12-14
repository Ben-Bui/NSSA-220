#!/bin/bash
spawn(){
	#spawn processes
	./APM1 $1 &
	pid1=$!
	echo "started proc1: ${pid1}"
	./APM2 $1 &
	pid2=$!
	echo "started proc2: ${pid2}"
	./APM3 $1 &
	pid3=$!
	echo "started proc3: ${pid3}"
	./APM4 $1 &
	pid4=$!
	echo "started proc4: ${pid4}"
	./APM5 $1 &
	pid5=$!
	echo "started proc5: ${pid5}"
	./APM6 $1 &
	pid6=$!
	echo "started proc6: ${pid6}"

	ifstat -a -d 1	
}
collect_process_level_metrics(){
	echo "$SECOND ,` ps -aux |awk '{print $4}'`"  >> APM1_metrics.csv
	echo "$SECOND ,` ps -aux |awk '{print $4}'`"  >> APM2_metrics.csv
	echo "$SECOND ,` ps -aux |awk '{print $4}'`"  >> APM3_metrics.csv
	echo "$SECOND ,` ps -aux |awk '{print $4}'`"  >> APM4_metrics.csv
	echo "$SECOND ,` ps -aux |awk '{print $4}'`"  >> APM5_metrics.csv
	echo "$SECOND ,` ps -aux |awk '{print $4}'`"  >> APM6_metrics.csv
}
collect_system_level_metrics(){
Disk_writes=iostat |grep nvme0n1 |awk '{print $4}'

	echo "$SECOND ,$Disk_writes"  >> system_metrics.csv
}
cleanup(){

	#kill proceess ..re
	kill -9 $pid1
	kill -9 $pid2 
	kill -9 $pid3
	kill -9 $pid4
	kill -9 $pid5
	kill -9 $pid6
	pkill -f -9 "ifstat"
exit $?
}
#clean up
 	trap cleanup SIGINT
#echo "Enter the IP address for the NIC"
read -p "Enter ip address " IP_ADDRESS
spawn "$IP_ADDRESS"
#while loop start for running the script every 5 seconds
SECONDS=0
	while true ;
	do
		#sleep for 5 seconds
		sleep 5;
		if [[ $SECOND -ge 300 ]]; then
			cleanup
		fi
		echo "sleeping 5 seconds"
		duration=$SECONDS

		#collect process level metrics
		collect_process_level_metrics
		#collect system level metrics
		collect_system_level_metrics
		#end of while loop
	done