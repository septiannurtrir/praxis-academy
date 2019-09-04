#!/usr/bin/python

def SelectionSort(val): # menggunakan command selectionsort untuk memilih elemen dengan nilai paling rendah dan menukarnya dengan elemen ke- yang ditentukan.
		for isi in range(len(val)-1,0,-1): # memulai command for loop
			Max=0 
			for lokasi in range(1,isi+1):
				if val[lokasi]>val[Max]:
					Max = lokasi

			temp = val[isi]
			val[isi] = val[Max]
			val[Max] = temp

DaftarAngka = [23,7,32,99,4,15,11,20] # mendefinisikan list data menggunakan 'DaftarAngka'
# SelectionSort(DaftarAngka)
# print(DaftarAngka)
