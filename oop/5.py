'''
Author : Mochammad Ihza Rizky Karim
'''
# Encapsulation / Enkapsulasi

class manusia():
	def __init__(self):
		self.__tinggi = 160 # private

	def dukur(self):
		print("Tinggi Manusia : {}".format(self.__tinggi))

	# untuk set nilai tinggi yang diganti dengan Dukur
	def setDukur(self,Dukur):
		self.__tinggi = Dukur

manusia1 = manusia()
manusia1.dukur()

# Mengubah Tinggi
manusia1.__tinggi = 200
manusia1.dukur()

# Menggunakan Setter
manusia1.setDukur(200)
manusia1.dukur()

'''
Output :

Tinggi Manusia : 160
Tinggi Manusia : 160
Tinggi Manusia : 200

'''
