'''
Author : Mochammad Ihza Rizky Karim
'''

# Magic Methods

class OrangTua():
	def __init__(self,nama):
		self.nama = nama
	
	def __repr__(self):
		return "Nama Orang Tua saya : {}".format(self.nama)
	
	def __add__(self,lainnya):
		return self.nama + lainnya
	
ortu1 = OrangTua("Budi")
print(ortu1)
print(ortu1 + " Andi")

'''
Output :

Tanpa magic method __repr__ :

<__main__.OrangTua object at 0x7f29ff47fd30>
Budi Andi

Menggunakan magic method __repr__  :

Nama Orang Tua saya : Budi
Budi Andi

Tanpa Magic Method __add__ :

Nama Orang Tua saya : Budi
Traceback (most recent call last):
  File "8.py", line 19, in <module>
    print(ortu1 + " Andi")
TypeError: unsupported operand type(s) for +: 'OrangTua' and 'str'

Menggunakan Magic Method __add__ :

Nama Orang Tua saya : Budi
Budi Andi

'''
