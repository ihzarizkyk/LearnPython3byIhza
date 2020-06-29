'''
Author : Mochammad Ihza Rizky Karim, userghost
'''

print(".: Program Kalkulator Sederhana :.")
print("Program ini dapat menghitung operasi matematika sederhana dari dua bilangan yang diinputkan.")
print("Silahkan pilih salah satu operasi matematika berikut ini:")
print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian")
pilihan = int(input("Masukan Nomor Pilihan anda : "))
bil1 = int(input("Input Bilangan Pertama : "))
bil2 = int(input("Input Bilangan Kedua : "))
if(pilihan==1):
    print("Hasil Penjumlahan adalah ",bil1+bil2)
elif (pilihan==2):
    print("Hasil Pengurangan adalah ",bil1-bil2)
elif (pilihan==3):
    print("Hasil Perkalian adalah ",bil1*bil2)
elif (pilihan==4):
    print("Hasil Pembagian adalah ",bil1/bil2)
