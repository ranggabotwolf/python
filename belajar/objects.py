# Objects
# Semua yang ada dalam Python adalah object, walaupun itu str, int, float, list, dictionary, tuples, dll
# Object memiliki atribut dan method yang bisa diakses melalui dot (.) syntax
# Contoh seperti berikut:
age = 9
# Variable age sekarang mendapatkan akses ke properti dan method yang didefinisikan untuk semua int objek
# Contohnya adalah akses ke real dan bagian imaginary dari angka dalam variable age

print(age.real)
# Code diatas akan menampilkan bilangan real dari nilai yang sudah dideklarasikan dalam variable age, yaitu 9
print(age.imag)
# Code diatas akan menampilkan bilangan imaginary dari nilai yang sudah dideklarasikan dalam variable age, yaitu 0
print(age.bit_length())
# Code diatas akan menampilkan panjang nilai dari age dalam binary, yaitu 4

# Kita juga bisa melakukan yang lainnya seperti:
items = [1, 2]
# Kita mendeklarasikan dicrionary yang bernama items yang memuat value 1 dan 2 didalamnya
items.append(4)
# Lalu kita menambahkan value 4 dengan function append
items.append(3)
# Kita menambahkan value lagi kedalam dictionary items yang bernilai 3
items.pop()
# Lalu kita menghapus value terakhir yang ditambahkan dalam dictionary items, yaitu 3
print(items[0],items[1], items[2], items)
# Nilai yang tampil seharusnya adalah 1, 2, dan 4

# Method yang tersedia dalam object tergantung pada tipe pada value
# id global dalam Python memungkinkan kita menginspect / mengetahui lokasi dalam memory u/ object tertentu

print(id(items))
# Code diatas akan menampilkan lokasi / tempat variable items di dalam memory

# Bisa berubah / tidaknya suatu nilai / valu dalam object bergantung pada object itu sendiri
# Jika object menyediakan method untuk merubah value dalam object, maka object tersebut bisa berubah
# Tapi bila tidak, maka object tersebut tidak bisa berubah value nya
# Banyak tipe yang didefinisikan oleh Python adalah object yang immutable / tidak bisa dirubah
# Contohnya adalah int adalah tipe yang immutable, karena tidak ada method untuk merubah value

# Seperti contoh berikut:
umur = 9
umur = umur + 1
# Bila kita increment umur seperti code di atas, sebenarnya kita membuat sebuah value baru
# Dan itu tidak akan menjadi object yang sama lagi
# Karena kita harus membuat sesuatu yang baru untuk dipindahkan / diubah
print(umur)

# Tapi bila dalam dictionary, objectnya tetap sama dan hanya berubah beberapa bagian di dalamnya / value nya
