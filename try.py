#REFERENSI SITUS BELAJAR PYTHON :

#https://www.w3schools.com/python/
#https://belajarpython.com/
#https://www.tutorialspoint.com/python/


# #1.Membuat Variabel dan Mengeluarkan Output

# nama = "Mochammad Ihza Rizky Karim"
# umur = 19
# print(nama,umur)


#2.Membuat List dan Perulangan FOR

# #INI CONTOH LIST 
# data = ["satu","dua","tiga"]
# data1 = [1,2,3]

# cara print satu nilai
# print(data[0]) 
# print(data[1]) 
# print(data[2]) 

# cara print semua nilai sekaligus dengan for
# for i in data:
# 	print(i)
# output : satu,dua,tiga

# data2 = [1,2,3] + [4,5,6] #Concatenation atau penyambung
# data2.append("7")
# data2.append("8")

# for i in data2:
# 	print(i)

# data3 = ['tes']*10 #Repeat

# for y in data3:
# 	print(y)

# for x in data:
# 	print(x)

#Perulangan WHILE

# hitung = 0
# while(hitung<10):
# 	print("Hitung Angka ke-",hitung)
# 	hitung = hitung + 1
# print("Selesai")





# #3.Kalkulator Sederhana
# bil1 = int(input("Masukkan Bilangan Pertama : "))
# bil2 = int(input("Masukkan Bilangan Kedua : "))
# print("Pilih Operasi Perhitungan\n","1.Tambah\n","2.Kurang\n","3.Bagi\n","4.Kali\n")
# pilihan = int(input("Pilih Operasi diatas : "))

# if(pilihan == 1):
# 	print(bil1+bil2)
# elif(pilihan == 2):
# 	print(bil1-bil2)
# elif(pilihan == 3):
# 	print(bil1/bil2)
# elif(pilihan == 4):
# 	print(bil1*bil2)

# #PROGRAM DISKON

# diskon = 50/100
# harga = int(input("Masukkan Harga Barang : "))
# print(int(harga*diskon))

# #4.Untuk Cek Tipe Data 
# a = 20
# print(type(a))

# odds = [x for x in range(20) if x % 2 == 0]
# print(odds)

# 5.Python Casting

# int()
# float()
# str()

# #6.String

# kata = "asdasdasdasdasd"
# print(len(kata),"Huruf")

# #LOWER CASE, UPPER CASE & CAPITALIZE
# kata = "INI HURUF KAPITAL"
# kalimat = "ini merupakan kalimat"
# print(kata.lower())
# print(kata.capitalize())
# print(kalimat.upper())

# #Program Ulang Kata/Kalimat
# print("Program Ulang Kata/Kalimat")
# isi = str(input("Isi Kalimat disini : "))
# print("Ulang sebanyak :\n","1.10 Kali\n","2.20 Kali \n","3.30 Kali")
# berapa = int(input("Pilih Berapa Kali : "))

# if(berapa == 1):
# 	for x in isi:
# 		print(x* 10)
# elif(berapa == 2):
# 	for x in isi:
# 		print(x* 20)
# elif(berapa == 3):
# 	for x in isi:
# 		print(x* 30)
# else:
# 	print("ERROR")

# 7.Date

# import time

# local = time.localtime(time.time())
# general = time.time()
# print(local)
# print(general)

# 8.Function

# def fungsi():
# 	print("ini fungsi python")
# fungsi()

#  9.Tuples 

#  tuple hampir sama seperti list, tetapi perbedaannya tuple tidak bisa diubah isinya sedangkan
#  list bisa diubah isinya.

# tuple1 = [1,2,3,4]
# tuple2 = [5,6,7,8]

# print(tuple1[0])
# print(tuple2[1])

#  # Cara Menghapus Tuple

# # del(tuple1)

# print(tuple1[0])


# Pandas :
# - DataFrame
# - Series
# - Panel

#  *index

# import pandas as pd 
# import numpy as np 

# d = np.array([['Nita','20','Malang'],['Ihza','19','Sidoarjo'],['Amir','18','Surabaya']])
# result = pd.DataFrame(data=d)
# print(result)

# 10.Class

# class player:
# 	def __ini__(self,nama,umur):
# 	self.nama = nama
# 	self.umur = umur
# p1 = player("Ihza",19)

# print(p1.nama)
# print(p1.umur)

# 11.File I/O

# file = open("chat.txt","wb")
# print(file)

# 12.Input

# Input

# nama = input("Masukkan Nama Anda : ")


# #Input String

# string = str(input("Masukkan String : "))

# #Input Integer atau Angka

# integer = int(input("Masukkan Angka Integer : "))

# print(nama)
# print(string)
# print(integer)

# #NUMPY & PANDAS PYTHON

# import numpy as np
# import pandas as pd

# #Basic Array Numpy
# satu = np.array(["satu","dua","tiga"])
# print(satu)

# #Array Numpy & DataFrame Pandas
# data = np.array([["nama","umur","kota"],
# 				["Ihza",19,"surabaya"],
# 				["anton",20,"malang"],
# 				["andi",21,"gresik"]])
# result = pd.DataFrame(data = data)
# print(result)

# #3D Array Numpy
# tigadimen = np.arange(12).reshape(2,2,3)
# print(tigadimen) 

# #Memulai array 1 - 100
# dataset = np.arange(1,101)
# print(dataset)

# #Mencari Mean

# datamean = np.array([[1,2,3],[4,5,6],[7,8,9]])
# mean = np.mean(data)
# print(datamean)

# #Mencari Median

# datamedian = np.array([[1,2,3],[4,5,6],[7,8,9]])
# median = np.median(datamedian)
# print(median)

#SCIPY Python

# from scipy import misc
# import matplotlib.pyplot as plt

# face = misc.face()
# plt.imshow(face)
# plt.show()

# class Student:
# 	def __init__(self, name, age):
# 		name = self.name
# 		age = self.age

# 	Siswa = siswa("Abdul", 15)
# 	print('siswa')