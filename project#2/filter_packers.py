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
	read_write("Node2.txt",2)
	read_write("Node3.txt",3)
	read_write("Node4.txt",4)

#filter()