'''
Author : Mochammad Ihza Rizky Karim
'''
import time

def pomodoro(mulai_mnt,mulai_dtk):
# total detik 
	total_dtk = mulai_mnt * 60 + mulai_dtk

	while(total_dtk):

	'''
	fungsi dari divmod untuk membagi jumlah menit dengan 60 detik
	dan menyimpan sisa bagi

	02d artinya tampilkan 2 digit nomor dari menit dan detik
	'''
		mins, secs = divmod(total_dtk, 60)
		print(f'{mins:02d}:{secs:02d}', end='\r')
	'''
	fungsi sleep untuk menunda waktu eksekusi
	'''
		time.sleep(1)
		total_dtk -= 1
	print("----POMODORO SELESAI----")

if(__name__  == '__main__'):
	pomodoro(25,00)
