def compute(ip,L,fn) :
	print('called compute function in compute_metrics.py')

def get_num(x):
    return int(''.join(num for num in x if num.isdigit()))
    
def compute_metric(ip,L,fn):
    request_sent_count=0
    request_received_count=0
    
    reply_sent_count=0
    reply_received_count=0
    
    request_byte_sent_count=0
    request_byte_received_count=0
    
    request_data_sent_count=0
    request_data_received_count=0
    
    count1=0
    total_time_1=0
    
    count2=0
    total_time_2=0
    
    avg_rtt=0
    avg_reply_delay=0
    
    request_throughput=0
    request_goodput=0
    hop_count = 0
    orginal_hop = 129
    
    
    
    for item in L :
            if item[8] == "reply":
                        if item[2] == ip :
                            reply_sent_count +=1

                        elif item[3] == ip :
                            reply_received_count += 1

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


            for i in range(0,len(L)):
                if L[i][8] == "request" :
                    if L[i][2] == ip :
                        count1 += 1
                        total_time_1 += (float(L[i+1][1]))-(float(L[i][1]))

            for i in range(0,len(L)):
                if L[i][8] == "request" :
                    if L[i][3] == ip :
                        count2 += 1
                        total_time_2 += (float(L[i+1][1]))-(float(L[i][1]))			
            
            for i in range(0,len(L)):
                if L[i][8] == "reply" :
                    if L[i][3] == ip :
                        hop_count += (orginal_hop - get_num(L[i][11]))
                        

            
            avg_rtt = (total_time_1 / count1)*1000 
            request_throughput = (request_byte_sent_count / total_time_1)/1000
            request_goodput = (request_data_sent_count / total_time_1)/1000 
            avg_reply_delay = (total_time_2/count2) * 1000000 
            avg_hop = float(hop_count)/float(request_sent_count) 

            return(request_sent_count,request_received_count,reply_sent_count,reply_received_count,round(request_byte_sent_count,2),round(request_data_sent_count,2),round(request_byte_received_count,2),round(request_data_received_count,2),round(avg_rtt,2),round(request_throughput,2),round(request_goodput,2),round(avg_reply_delay,2,),round(avg_hop,2))
