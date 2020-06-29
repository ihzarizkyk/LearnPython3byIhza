'''
Author : Mochammad Ihza Rizky Karim
'''

user = ("admin")
varpass = ("ihza")
count = 1

while count <= 3:
    username = input("Masukkann Username anda : ")
    password = input("Masukkan Password anda : ")

    if (username == "admin" and password == "ihza"):
        print("Anda Berhasil Login")
        break

    else:
        print ("Anda dipercobaan ke-",count)
        count = count+1
    if count>3:
        print("Anda Telah melakukan percobaan login sebanyak 3 kali,silahkan coba lagi kapan-kapan! ")
