import numpy as np
import matplotlib.pyplot as plt

#siapkan variable
arrdata = []
completedata = []
countload = 0
#ambil data line per line 
arrdata = open("foodprice.txt", "r")
#parsing 1 per 1 data dari setiap line 
for x in arrdata:
#tidak perlu proses data pertama karena hanya kolom baris
	if (countload):
		#parsing data , ganti jika string yg tidak perlu dengan kosong , split dengan \t untuk membagi setiap kolom
		completedata.append(x.replace("\n","").split("\t"))
	#itung lanjut bosque
	countload += 1
#berapa banyak data plain text menjijikan ini
print(countload,"data berhasil diload")
#sort secara sederhana (karena ada data taggal di kolom pertama maka itulah yg di sorting)
a = np.array(completedata)
#np.sort(a.view('M,U,U,U,U'), order=['f0'])
a = a[a[:,4].argsort()]
#tampilkan hanya 100 data
#kalo mau semua tinggal ganti ini
priceall = []
tgl = []
pricetotal = 0
for d in range(countload-1):
	priceall.append(int(completedata[d][4]))
	tgl.append(completedata[d][2]) #ini mbak indexnya
	pricetotal += int(completedata[d][4])
b = np.array(priceall)
indextengah = len(priceall)//2
priceall.sort()
if(not len(priceall)%2):
	median = (priceall[indextengah-1] + priceall[indextengah]) / 2.0
else:
	median =  priceall[indextengah]
print("Mean: Rp",round(pricetotal/countload))
print("Median: Rp",median)
print("q1: Rp", np.percentile(b, 25))
print("q2: Rp", np.percentile(b, 50))
print("q3: Rp", np.percentile(b, 75))
# x axis values 
x = priceall
# corresponding y axis values 
y = tgl
# plotting the points  
plt.plot(x, y) 
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Grafik Proccess Data Food!') 
# function to show the plot 
plt.show()