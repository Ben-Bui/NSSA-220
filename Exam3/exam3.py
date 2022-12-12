from scapy.all import*

packets = rdpcap('TeddyBallgame.pcap')
packets[ICMP].summary()

def compute_metric(ip,L,fn):
    request_sent_count=0
    request_received_count=0
   
    request_byte_sent_count=0
    request_byte_received_count=0
    
    request_data_sent_count=0
    request_data_received_count=0

    for item in L :
            if item[8] == "request":
                        if item[2] == ip :
                            request_sent_count += 1
                            request_byte_sent_count += int(item[5])
                            request_data_sent_count += int(item[5]) - 42    

                        elif item[3] == ip :
                            request_received_count += 1
                            request_byte_received_count += int(item[5])
                            request_data_received_count += int(item[5]) -42 
                            
            elif item[3] == ip :
                        request_received_count += 1 
                        request_byte_received_count += int(item[5])
                        request_data_received_count += int(item[5]) - 42 
            return(request_sent_count,request_received_count,round(request_byte_sent_count,2),round(request_data_sent_count,2),round(request_byte_received_count,2),round(request_data_received_count,2))

L1 = []

nl="\n"


(a,b,c,d,e,f,g,h,i,j,k,l,m) = compute_metric("192.168.100.2",L1,"TeddyBallgame")
file = open(filename,"w")
file.write("TeddyBallgame")
file.write(nl)
file.write("Echo Requests Sent,Echo Requests Recieved,Echo Replies Sent,Echo Replies Recieved"+ nl )
file.write(str(a)+","+str(b)+","+str(c)+","+str(d)+nl)
file.write("Echo Request Bytes sent (bytes),Echo Request Data Sent (bytes)"+ nl)
file.write(str(e)+","+str(f)+nl)
file.write("Echo Request Bytes Recieved (bytes),Echo Request Data Recieved (bytes)"+nl)
file.write(str(g)+","+str(h)+nl)
file.write(nl)
f.close()
