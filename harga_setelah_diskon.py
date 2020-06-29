'''
Author : Mochammad Ihza Rizky Karim
'''

harga_asli = int(input("Masukkan Harga Barang : "))
potongan = 20/100 * harga_asli
harga = round(harga_asli-potongan)
print("Harga Barang Setelah Diskon adalah ",harga)
