# map(), filter(), and reduce()
from functools import reduce

# map digunakan function ke setiap item dalam item yang dapat diubah, seperti list
# dan membuat list baru dengan jumlah item yang sama dengan sebelumnya
# tetapi value dari tiap itemnya bisa berubah / dirubah
# seperti contoh berikut :


# Ini adalah list
numbers = [1, 2, 3]


# Ini adalah function
def double(a):
    return a * 2


result = map(double, numbers)

print(list(result))
# Maka hasil dari code diatas adalah [2, 4, 6]
# Jadi jika kita ingin menjalankan sebuah function ke setiap item dalam list, gunakan map

# Jika functionnya adalah 1 baris, biasanya menggunakan lambda function
# berikut adalah contoh bila menggunakan lambda function :

triple = lambda b: b * 3

result = map(triple, numbers)
print(list(result))
# Hasil dari code diatas adalah [3, 6, 9]

# Kita juga bisa menggunakannya seperti ini :

result = map(lambda c: c * 5, numbers)
# Tanpa perlu mendeklarasikan lambda ke dalam variable, tapi langsung ke dalam function
print(list(result))
# Hasil dari code diatas adalah [5, 10, 15]

print("\n")
# filter()
# filter mengambil item yang dapat diubah, dan return sebagai filter object
# yang mana bisa diubah juga tapi tanpa beberapa item original (item yang belum diubah)
# Kita bisa melakukannya dengan cara returning True atau False dari filtering function


# dibawah ini contoh filtering function
# Kita akan mengecek jika item yang tampil adalah Even
def isEven(n):
    return n % 2 == 0


# Jadi jika n bisa dibagi 2 maka Even dan return True
# tapi jika n tidak bisa dibagi 2 maka Odd dan return False

# Dan setiap Even akan ditambahkan ke result dengan code dibawah
# sementara Odd tidak ditambahkan ke result
# Jadi sebenarnya kita memfilter list berdasarkan function ini, isEven function
result = filter(isEven, numbers)
print(list(result))
# Dan ketika kita print, maka hasilnya adalah 2
# Kenapa hanya 2 saja?
# Karena dari list numbers, yaitu 1, 2, 3, yang genap (Even) hanya 2 saja

# Kita juga bisa menggunakan lambda function seperti berikut :
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = filter(lambda n: n % 2 == 0, numbers2)
print(list(result2))
# Hasil dari code diatas adalah [2, 4, 6, 8, 10]

print("\n")
# reduce()
# reduce digunakan untuk menghitung value dari sequence, seperti list
expenses = [("Dinner", 90), ("Car Repair", 150)]
# Contohnya kita mempunyai list dari expenses yang disimpan sebagai Tuples
# Kita ingin menghitung penjumlahan dari property tersebut dalam setiap Tuples
# Dalam kasus ini adalah biaya dari tiap expenses
sum = 0
for expense in expenses:
    sum += expense[1]
# contoh code diatas adalah bila kita tidak menggunakan reduce
print(sum)
# Hasil penjumlahan dari code diatas adalah 240

# Berikut kita akan menggunakan reduce
# reduce berbeda dengan map dan filter
# reduce tidak otomatis ada seperti map dan filter
# Kita harus mengimportnya dari tools function library standard
# Kita sudah mengimport reduce pada baris ke 2
expenses2 = [("Cuci Motor", 10000), ("Cuci Mobil", 30000)]
sum2 = reduce(lambda a, b: a[1] + b[1], expenses2)
# reduce sebenarnya sama saja berusaha menambahkan setiap items dalam list
# dan mengurangi i index dan menjadikannya 1 value
print(sum2)
