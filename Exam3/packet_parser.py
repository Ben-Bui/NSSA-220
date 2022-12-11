def parse(fn,L) :
    print('called parse function in packet_parser.py')
    reader(fn,L)

def reader(fn, L):
	f = open(fn, "r")
	ls = f.readlines()

	for l in ls:
		L.append(l.stirp().split())

	f.close()