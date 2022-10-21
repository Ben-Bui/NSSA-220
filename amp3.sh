#!/bin/bash
run(){
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

process_level_metrics(){
	echo "$duration ,` ps -aux |awk -v r=$pid1 '$2 == r'|awk '{print $3}' `, `ps -aux |awk -v r=$pid1 '$2 == r'|awk '{print $4}'`"  >> APM1_metrics.csv
	echo "$duration ,` ps -aux |awk -v r=$pid2 '$2 == r'|awk '{print $3}' `, `ps -aux |awk -v r=$pid2 '$2 == r'|awk '{print $4}'`"  >> APM2_metrics.csv
	echo "$duration ,` ps -aux |awk -v r=$pid3 '$2 == r'|awk '{print $3}' `, `ps -aux |awk -v r=$pid3 '$2 == r'|awk '{print $4}'`"  >> APM3_metrics.csv
	echo "$duration ,` ps -aux |awk -v r=$pid4 '$2 == r'|awk '{print $3}' `, `ps -aux |awk -v r=$pid4 '$2 == r'|awk '{print $4}'`"  >> APM4_metrics.csv
	echo "$duration ,` ps -aux |awk -v r=$pid5 '$2 == r'|awk '{print $3}' `, `ps -aux |awk -v r=$pid5 '$2 == r'|awk '{print $4}'`"  >> APM5_metrics.csv
	echo "$duration ,` ps -aux |awk -v r=$pid6 '$2 == r'|awk '{print $3}' `, `ps -aux |awk -v r=$pid6 '$2 == r'|awk '{print $4}'`"  >> APM6_metrics.csv
}

system_level_metrics(){
	RX_TX_datarate=`ifstat |grep ens160|awk '{print $7","$9}'|sed 's/K//g'`
	Disk_writes=`iostat |grep nvme0n1  |awk '{print $4}'`
	Disk_capacity=$(df | grep /dev/shm | awk '{print $4}')

	echo "$duration ,$RX_TX_datarate,$Disk_writes,$Disk_capacity"  >> system_metrics.csv
}

cleanup(){
	kill -9 $pid1
	kill -9 $pid2 
	kill -9 $pid3
	kill -9 $pid4
	kill -9 $pid5
	kill -9 $pid6
	pkill -f -9 "ifstat"
exit $?
}

trap cleanup SIGINT

ip=$(ifconfig ens160 | grep 'inet' | head -n 1 | awk '{print $2}')

run "$ip"

SECONDS=0
	while true ;
	do
		if [[ $duration -eq 300 ]]; then
			cleanup
		fi
		echo "sleeping 5 seconds"
		duration=$SECONDS

		process_level_metrics

		system_level_metrics

		sleep 5;
	done