nama_nasabah = ['Anita','Budi','Cahya','Didit','Erni','Fahri']
saldo = [[2500000,5000000,1000000,4000000],#Anita
        [2500000,4000000,750000,3000000],#Budi
        [2000000,2000000,750000,4500000],#Cahya
        [2000000,1000000,750000,235000],#Didit
        [2000000,500000,750000,1250000],#Erni
        [2500000,750000,500000,440000]]#Fahri

iteration = 0
nasabah = [0,0,0,0,0,0]


for i in saldo:
    for x in i:
        nasabah[iteration]+=x
    iteration+=1

temp = 0
for i in nasabah:
    print("Total tabungan {} \t: Rp. {}".format(nama_nasabah[temp],i))
    temp += 1

nama_max = ''
nama_min = ''
saldo_max = 0
saldo_min = nasabah[0]

for i in range(0,6):
    if saldo_min > nasabah[i]:
        saldo_min = nasabah[i]
        nama_min = nama_nasabah[i]
    if saldo_max < nasabah[i]:
        saldo_max = nasabah[i]
        nama_max = nama_nasabah[i]
print()
print("Nasabah dengan total tabungan paling sedikit adalah {} dengan total Rp.{}".format(nama_min,saldo_min))
print("Nasabah dengan total tabungan paling banyak adalah {} dengan total Rp.{}".format(nama_max,saldo_max))

