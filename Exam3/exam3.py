from scapy.all import*

packets = rdpcap('TeddyBallgame.pcap')
packets[ICMP].summary()

#make a counter receive bytes and data
recieve = 0
data = 0
bytes = 0

for packet in packets :
		recieve += 1
ip_packet = 1

for packet in ip_pkts:
     if ip_packet.haslayer(ICMP) and ip_packet[ICMP].type() == "8" and ip_packet[IP].dst = '192.168.100.2'

print("Echo Request received from 192.168.100.2 =" + recieve)

#quer2
for packet in pkts:
     if packet.haslayer(ICMP) and packet[ICMP].type() == "8" and packet[IP].dst = '192.168.200.2'

bytes += packet[IP].len()
data += packet[ICMP].load()

print(bytes + data)
