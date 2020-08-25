'''
Author : Mochammad Ihza Rizky Karim
'''

# Overriding Method

class OrangTua():
	def perilaku(self):
		print("ini perilaku Orang Tua")

class Anak(OrangTua):
	def perilaku(self):
		print("ini perilaku Anak")

perilaku1 = OrangTua()
perilaku2 = Anak()

perilaku1.perilaku()
perilaku2.perilaku()