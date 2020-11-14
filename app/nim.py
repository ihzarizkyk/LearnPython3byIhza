nim = int(input("Masukkan NIM Anda : "))
data = [([1204190054,1204190057,1204190055],
		 ["Rizky","Budi","Andi"],
		 [100,200,300])]

if(nim == data[0][0][0]):
	print("Nama : ",data[0][1][0])
	print("Nilai : ",data[0][2][0])
elif(nim == data[0][0][1]):
	print("Nama : ",data[0][1][1])
	print("Nilai : ",data[0][2][1])
elif(nim == data[0][0][2]):
	print("Nama : ",data[0][1][2])
	print("Nilai : ",data[0][2][2])
else:
	print("Data Tidak ditemukan")
