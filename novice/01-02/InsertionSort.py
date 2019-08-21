#!/usr/bin/python

def InsertionSort(val): # menggunakan command insertionsort untuk menyortir data dengan sederhana.
		for index in range(1,len(val)): # memulai command for loop

			valueaktif = val[index]
			posisi = index

			while posisi>0 and val[posisi-1]>valueaktif: # menggunakan command while untuk menyesuaikan kondisi yang ditentukan.
				val[posisi]=val[posisi-1]
				posisi = posisi-1

			val[posisi]=valueaktif

DaftarAngka = [23,7,32,99,4,15,11,20] # mendefinisikan list data dengan 'DaftarAngka'
# InsertionSort(DaftarAngka)
# print(DaftarAngka)
