 #!/usr/bin/python

def BubbleSort(val):
	for passnum in range(len(val)-1,0,-1):
		for i in range(passnum):
			if val[i]>val[i+1]:
				temp = val[i]
				val[i] = val[i+1]
				val[i+1] = temp

DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)
print(DaftarAngka)
