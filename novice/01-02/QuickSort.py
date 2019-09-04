def quickshort(a,start,end): # mengurutkan data yang paling cepat
	if start<end:
		pindex = partition(a,start,end)
		quickshort(a,start,pindex-1)
		quickshort(a,pindex+1,end)

def partition(a,start,end):
		middle = int(end/2)
		pivot = a[middle]
		pindex = start
		for i in range(start,middle): # mulai command for loop
				if a[i]>=pivot: # mulai menggunakan if sesuai kondisi
						a[i],a[pindex]=a[pindex],a[i]
						pindex = pindex + 1
						a[pindex],a[middle]=a[middle],a[pindex]
		print(a)
		return pindex

a = [23,7,32,99,4,15,11,20] # mendefinisikan list data dengan 'a'
quickshort(a,0,len(a)-1) # mengurutkan dan menghitung panjang data sesuai dengan kondisi yang ditentukan dengan 'len'
