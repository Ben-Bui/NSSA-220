def compute(ip,L,fn) :
	print('called compute function in compute_metrics.py')

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
