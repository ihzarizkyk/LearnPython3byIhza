'''
Author : Mochammad Ihza Rizky Karim
'''
import random

userpass = input("Masukkan Password : ")
simbol = "[]{}()*/-+"
nomor = "1234567890"
semua = userpass + simbol + nomor 

panjang = 12
password = "".join(random.sample(semua, panjang))
print("HASIL PASSWORD GENERATOR : ",password)
