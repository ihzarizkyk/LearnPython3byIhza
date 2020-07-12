'''
Author : Mochammad Ihza Rizky Karim
'''

class bio():
	def __init__(self,names,age,height):
		self.names = names
		self.age = age
		self.height = height

	def isi(self):
		print("Nama : ",self.names,",Umur : ",self.age,",Tinggi : ",self.height)


bio1 = bio("Ihza",19,166)
bio2 = bio("Rizky",20,167)
bio1.isi()
bio2.isi()

"""
Output :

Nama :  Ihza ,Umur :  19 ,Tinggi :  166
Nama :  Rizky ,Umur :  20 ,Tinggi :  167

"""
