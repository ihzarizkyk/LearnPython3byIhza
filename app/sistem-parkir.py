# Sistem Parkir
from timer import timer as tm
from random import randrange
from datetime import datetime
import threading
import numpy as np
import csv
import time
import random
import numpy as np

blok = 0
blok1 = 0 + 1
blok2 = 0 + 3
# tersedia1 = 0
# tersedia2 = 0
acak = [1,-1,0,1,0]
# x = np.arange(1)
# y = x.reshape(2,4)
parkir = 0
jawaban = "ya"
sekarang = time.asctime(time.localtime(time.time()))
now = datetime.now()
baru = now.strftime("%H:%M:%S")

def readFile(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            dataCSV = []
            for row in csv_reader:
                dataCSV.append(row)    
            csv_file.close()
            return dataCSV
        
    except IOError:
        print("The file",filename,"doesn't exist.")

def angka():
    filename = 'angka.csv'
    dataCSV = readFile('angka.csv')
    line = 0
    print
    for row in dataCSV:
        if(line == 0):
# g = np.array(row[0])
# x = g.reshape(1,1)
# print(x)
        	print(row[0])
#print(random.randrange(int(row[0]),0,int(row[0])))

# Durasi Awal
durasi = int(input("Masukkan Durasi simulasi (detik) : "))
print(durasi)

print("===== Selamat Datang di Parkir Mall Berkah =====")

while(jawaban == "ya"):
	jawaban = str(input("Apakah anda ingin parkir? "))
	parkir = parkir + 1
	blok1 = 0 + 1
	blok2 = 0 + 3
	print("Masuk Pada ",baru)
	print("Parkir tersedia di Lokasi {}-{}".format(blok1,blok2))
	print("====================================\n")

	if(parkir == 5):
		print("Maaf Parkir Sedang Penuh ",baru)
		parkir = parkir + 1
		if(parkir > 5):
			print("Masuk Pada ",baru)
			print("Parkir tersedia di Lokasi {}-{}".format(blok1,blok2))
			print("====================================\n")
			if(str(time.sleep(durasi)) >= str(durasi)):
				print("Masuk Pada ",baru)
				print("Parkir tersedia di Lokasi {}-{}".format(blok1,blok2))
				print("====================================\n")
				print("Simulasi berakhir pada ",baru)
				print("Kondisi Terakhir :\n","#########")
				angka()
				break

# buat file csv sendiri ya
