'''
Author : Mochammad Ihza Rizky Karim, userghost
'''

kas_awal = 500000000
nama_barang = input("Nama Barang : ")
jumlah_barang =int(input("Jumlah Barang : "))
harga_satuan = int(input("Harga Barang Satuan : "))
harga_total = harga_satuan * jumlah_barang
kas_updated = kas_awal-harga_total
print("Total Harga Barang adalah ",harga_total)
print("Sisa Uang kas adalah ",kas_updated)
if(kas_updated>100000000):
    pesan = "Ayo belanja Lagi"
elif (kas_updated<0):
    pesan = "Kalian Terlalu Boros"
else:
    pesan = "Kas Tersisa Kurang Dari Rp.100.000.000,-"
print("Pesan:",pesan)
