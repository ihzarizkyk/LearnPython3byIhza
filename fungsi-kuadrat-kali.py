'''
Author : Mochammad Ihza Rizky Karim
'''

#buat fungsi kuadrat yang didalamnya memuat parameter angka
def kuadrat(angka):
#lalu kembalikan nilai angka dan kuadratkan
	return angka*angka

#buat variabel nol sampe sembilan yang menyimpan fungsi kuadrat 
#beserta angka 0 - 9
nol = kuadrat(0)
satu = kuadrat(1)
dua = kuadrat(2)
tiga = kuadrat(3)
empat = kuadrat(4)
lima = kuadrat(5)
enam = kuadrat(6)
tujuh = kuadrat(7)
delapan = kuadrat(8)
sembilan = kuadrat(9)

#ini untuk mencetak output fungsi diatas
print("kuadrat dari 0 adalah ",nol)
print("kuadrat dari 1 adalah ",satu)
print("kuadrat dari 2 adalah ",dua)
print("kuadrat dari 3 adalah ",tiga)
print("kuadrat dari 4 adalah ",empat)
print("kuadrat dari 5 adalah ",lima)
print("kuadrat dari 6 adalah ",enam)
print("kuadrat dari 7 adalah ",tujuh)
print("kuadrat dari 8 adalah ",delapan)
print("kuadrat dari 9 adalah ",sembilan)


#ini menggunakan fungsi
#buat fungsi kali yang memuat 2 parameter argumen
def kali(bil1,bil2):
#buat perulangan dari bilangan 1 dan bilangan 2 dengan range 3 - 11 dengan
#jeda 2  
	for bil1 in range(3,13,2):
		print("\t")
		  for bil2 in range(3,13,2):
#print dengan format berikut
			 print('{}*{} = {}\t'.format(bil1,bil2,bil1*bil2))
      
