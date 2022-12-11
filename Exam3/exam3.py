
from filter_packets import *
from packet_parser import *
from compute_metrics import *

L1 = []

nl="\n"

filter()

parse("TeddyBallgame_filtered.txt", L1)

filename="output.csv"

(a,b,c,d,e,f,g,h,i,j,k,l,m) = compute("192.168.100.2",L1,"TeddyBallgame_filtered.txt")
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
f.close()