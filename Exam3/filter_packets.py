def read_write(fn, num):
    filterfile = "TeddyBallgame" + str(num) + "_filtered.txt"
    f = open(fn, "r")
    aFile = open(filterfile, "w")
    ls = f.readlines()

    for l in ls:
        if 'ICMP' in l:
            aFile.write(l)
    f.close()
    aFile.close()    


def filter():
	read_write("TeddyBallgame.txt",1)