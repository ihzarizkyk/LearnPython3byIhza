'''
Author : Mochammad Ihza Rizky Karim
'''

# membuat class gedung
class gedung:

# class variable
	jumlah_gedung = 0

# membuat method constructor
	def __init__(self,nama,jumlah):
	# data member
		self.nama = nama 
		self.jumlah = jumlah
		gedung.jumlah_gedung+=1

# membuat method nama_gedung
	def nama_gedung(self):
		print("Nama Gedung : ",self.nama, ",Jumlah Lantai : ",self.jumlah,", Jumlah Gedung : ", gedung.jumlah_gedung)

# instansiasi object gedung1 dan class gedung
gedung1 = gedung("Gedung Casablanca",12)
gedung2 = gedung("Gedung Sate",3)

# mengeluarkan output dari object gedung1 dan gedung2
gedung1.nama_gedung()
gedung2.nama_gedung()

'''
Output :

Nama Gedung :  Gedung Casablanca ,Jumlah Lantai :  12 , Jumlah Gedung :  2
Nama Gedung :  Gedung Sate ,Jumlah Lantai :  3 , Jumlah Gedung :  2

'''