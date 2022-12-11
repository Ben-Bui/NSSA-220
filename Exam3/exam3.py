def read_write(fn, num):
    filterfile = "Node" + str(num) + "_filtered.txt"
    f = open(fn, "r")
    aFile = open(filterfile, "w")
    ls = f.readlines()

    for l in ls:
        if 'ICMP' in l:
            aFile.write(l)
    f.close()
    aFile.close()    


def filter():
	read_write("Node1.txt",1)

def parse(fn,L) :
    print('parse function in')
    reader(fn,L)

def reader(fn, L):
	f = open(fn, "r")
	ls = f.readlines()

	for l in ls:
		L.append(l.stirp().split())

	f.close()def compute(ip,L,fname) :
	print(' compute function in ')

	
	return(compute_metric(ip,L,fname))
def compute_metric(ip,L,fname):
	request_sent_count=0
	request_rcvd_count=0
	bytes_sent=0
	bytes_rcvd=0
	data_sent=0
	data_rcvd=0

    for item in L :
		if item[8] == "request" :
			if item[2] == ip :
				request_sent_count += 1 
				bytes_sent += int(item[5])
				data_sent += int(item[5]) - 42

		
			elif item[3] == ip :
				request_rcvd_count += 1 
				bytes_rcvd += int(item[5]) 
				data_rcvd += int(item[5]) - 42 

L1 = []
nl="\n"

filter()

parse("Node1_filtered.txt", L1)

filename="output.csv"

(a,b,c,d,e,f,g,h,i,j,k,l,m) = compute("192.168.100.2",L1,"Node1_filtered.txt")
file = open(filename,"w")
file.write("Node1")
file.write(nl)
file.write("Echo Requests Sent,Echo Requests Recieved,Echo Replies Sent,Echo Replies Recieved"+ nl )
file.write(str(a)+","+str(b)+","+str(c)+","+str(d)+nl)
file.write("Echo Request Bytes sent (bytes),Echo Request Data Sent (bytes)"+ nl)
file.write(str(e)+","+str(f)+nl)
file.write("Echo Request Bytes Recieved (bytes),Echo Request Data Recieved (bytes)"+nl)
file.write(str(g)+","+str(h)+nl)
file.write(nl)
file.write(nl)
file.close()

