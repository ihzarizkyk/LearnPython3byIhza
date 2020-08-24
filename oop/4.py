'''
Author : Mochammad Ihza Rizky Karim
'''

# inheritance (Pewarisan Class)

# Class Utama
class manusia:
	def __init__(self,nama):
		self.nama = nama

	def cek(self):
		return True

	def show_all(self):
		print("Saya Bernama : ",self.nama)


# Class Turunan
class person(manusia):

	def cek(self):
		return False

p1 = manusia("Ihza")
p2 = person("Rizky")

print(p1.show_all(),p1.cek())
print(p2.show_all(),p2.cek())

'''
OUTPUT :

Saya Bernama :  Ihza
None True
Saya Bernama :  Rizky
None False

'''