'''
Author : Mochammad Ihza Rizky Karim
'''

# Polymorphism

# simple example using len function

print(len("Polymorphism"))
print(len([0,1,2,3]))

'''
Menggunakan Fungsi len

Output : 

12 (Tipe Data String)
4 (Tipe Data List)
'''

# using class

class indonesia:
	def ibukota(self):
		print("Jakarta adalah Ibu Kota Negara Indonesia")
class malaysia:
	def ibukota(self):
		print("Kuala Lumpur adalah Ibu Kota Negara Malaysia")

negara1 = indonesia()
negara2 = malaysia()

for country in (negara1,negara2):
	country.ibukota()

'''
Output :

Jakarta adalah Ibu Kota Negara Indonesia
Kuala Lumpur adalah Ibu Kota Negara Malaysia

'''
