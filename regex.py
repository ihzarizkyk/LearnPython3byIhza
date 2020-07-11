# Author : Mochammad Ihza Rizky Karim
# Regular Expression (RegEx) Python 3

import re

# buat pola
pattern = "^i.......a$"

# buat string 
text = "indonesia"

# masukkan ke dalam fungsi match()
x = re.match(pattern,text)

if(x):
	print("String Sama")
else:
	print("String Tidak Sama")

'''

^ = mulai
$ = akhir

Output :

String Sama

'''