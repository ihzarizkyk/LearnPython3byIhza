print("PROGRAM KONVERSI SUHU")
print(" 1.Konversi ke Suhu Farenheit\n","2.Konversi ke Suhu Reamur\n","3.Konversi ke Suhu Kelvin")
suhu = int(input("Masukkan Suhu Celcius : "))
pilih = int(input("Pilih Mau Konversi ke? "))

if(pilih == 1):
	print((suhu*9/5)+32,"Farenheit")
elif(pilih == 2):
	print(int((4/5)*suhu),"Reamur")
elif(pilih == 3):
	print(suhu + 273.15,"Kelvin")
else:
	print("Pilihan Tidak Ada")