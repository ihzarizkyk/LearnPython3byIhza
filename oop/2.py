'''
Author : Mochammad Ihza Rizky Karim
'''

class mobil:
	# Class Body

# method __init__ untuk menginisiasi object dari kelas
	def __init__(self,merk,seri):
		self.merk = merk
		self.seri = seri

	# method

	def tampilkan(self):
		print("Merk Mobilnya : ",self.merk)
		print("Nomor Seri Mobil : ",self.seri)

#instansiasi object dari class

mobil1 = mobil("Mobil Avanza",2019)

# menampilkan instansiasi

mobil1.tampilkan()

'''
Output :

Merk Mobilnya :  Mobil Avanza
Nomor Seri Mobil :  2019
'''