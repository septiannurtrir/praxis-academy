def mergesort(a): # menggunakan command merge sort untuk mengurutkan data dengan cara penggabungan.
		print('memecah',a)
		n=len(a)
		if n<2: #
				return a
		else:
				mid=n//2
				left=a[:mid]
				right=a[mid:]

				mergesort(left)
				mergesort(right)
				i=0
				j=0
				k=0
				while i< len(left) and J<len(right): # menggunakan command while untuk menyesuaikan kondisi yang telah ditentukan.
						if left[i]>right[j]:
								a[k]=left[i]
								i=i+1
						else:
								a[k]=right[j]
								j=j+1
						k=k+1
				while i<len(left):
						a[k]=left[i]
						i=i+1
						k=k+1
				while j<len(right):
						a[k]=right[j]
						j=j+1
						k=k+1
a = [23,7,32,99,4,15,11,20] # mendefinisikan list data dengan 'a'
# MergedSort(DaftarAngka)
# Print(DaftarAngka)
