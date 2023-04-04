# Tuples
# Tuples adalah deklarasi yang tidak bisa diubah
nama = ("Rangga", "Putra", "Pratama", "lusiyanti", "Eka")

nama[1:2]
nama.index("Pratama")

len(nama)
print("Pratama" in nama)
print(sorted(nama, key=str.lower))

print("\n")
newTuple = nama + ("Love", "Forever")
print(newTuple)
print(sorted(newTuple, key=str.lower))

print("\n")
# Dictionaries
pacar = {"nama": "Eka", "umur": "26"}
# Code dibawah hanya akan menampilkan data nama yang ada dalam dictionary pacar
print(pacar["nama"])

# Code dibawah akan mengubah data dalam data pacar, bagian nama, yang sebelumnya Eka, menjadi Lusiyanti
pacar["nama"] = "Lusiyanti"
# Code dibawah akan menampilkan semua data yang ada dalam dictionary pacar
print(pacar)

# Bila ingin menampilkan suatu data dalam dictionary, dapat juga menggunakan code dibawah:
print(pacar.get("nama"))

print("\n")
hobi = {"Makan": "Mie Ayam", "Girlband": "Black Pink"}
# Kita juga bisa menampilkan data yang belum ada dalam dictionary, seperti contoh dibawah, warna adalah jenisnya, kuning adalah isinya
print(hobi.get("warna", "kuning"))
# Code diatas akan menampilkan warna kuning sebagai nilai / hasil default bila warna tidak ditemukan dalam dictionary


print("\n")
# Tapi, bila data yang akan ditampilkan sudah ada dalam dictionary, maka bila ketika di deklarasikan data baru dalam perintah print
# Maka yang ditampilkan tetap data yang ada dalam dictionary, bukan data yang di deklarasikan pada perintah print, seperti contoh dibawah:
hobi2 = {"Makan": "Mie Ayam", "Girlband": "Black Pink",
         "hobi": "Bernyanyi", "warna": "Pink"}
print(hobi2.get("warna", "kuning"))


print("\n")
# Code dibawah akan menampilkan data yang ingin ditampilkan lalu menghapusnya, pop = menghapus data
print(hobi2.pop("Makan"))
# Dan bila data dictionary hobi2 di print lagi, maka, data Makan : Mie Ayam telah hilang dalam dictionary, dihapus oleh pop
print(hobi2)

print("\n")
# Code dibawah akan menampilkan data yang terakhir kali ditambahkan dalam dictionary, lalu menghapusnya (itulah fungsi popitem)
print(hobi2.popitem())
# Dan bila kita print lagi data dictionary hobi2, maka, data warna : Pink juga akan hilang, karena sudah ditampilkan lalu dihapus dengan code diatas
print(hobi2)

print("\n")
print("hobi" in hobi2)
# Kita bisa juga mengecek apakah ada suatu key value yang ingin kita cek dalam dictionary seperti code diatas

print("\n")
# Kita juga bisa menampilkan key value apa saja yang ada di dalam dictionary seperti code dibawah:
print(hobi2.keys())
# Code diatas akan menampilkan hasil seperti berikut:
# dict_keys(['bla', 'bla', 'bla'), sesuai apa yang ada di dalam dictionary
print(list(hobi2.keys()))
# Kita juga bisa menampilkan hasil dalam bentuk list saja menggunakan code diatas

print("\n")
# Kita juga bisa menampilkan value / nilai dari masing-masing key value dalam dictionary seperti contoh dibawah:
print(hobi2.values())
# Code diatas sama hasilnya dengan code baris ke 64, perbedaannya hanya dalam code diatas yang akan tampil adalah value nya
print(list(hobi2.values()))
# Code diatas sama hasilnya dengan code baris ke 67, perbedaannya hanya dalam code diatas yang akan tampil adalah value nya

print("\n")
print(hobi2.items())
# Bila kita menggunakan code diatas, maka semua data dalam dictionary (key value dan value) akan tampil
print(list(hobi2.items()))
# Dan bila kita menggunakan code diatas, maka semua data dalam dictionary (key value dan value) akan tampil dalam bentuk list
print(len(hobi2))
# Kita juga bisa mengetahui berapa jumlah data dalam dictionary menggunakan code diatas

print("\n")
hobi2["Status"] = "Guru"
# Code diatas akan menambahkan data di dalam dictionary
print(hobi2)

# Kita juga bisa mengcopy dictionary hobi2 dengan code seperti berikut:
hobi2Copy = hobi2.copy()

print("\n")
# Kita juga bisa menghapus data dalam dictionary menggunakan code seperti berikut:
del hobi2["hobi"]
print(hobi2)

print("\n")
print(hobi2)
# Ketika hobi2Copy di tampilkan / di panggil menggunakan code dibawah, mengapa berbeda dengan code diatasnya
# Code diatas menampilkan Girlband dan Status, sementara dibawah ada 1 tambahaan data yaitu hobi, mengapa?
# Karenna code hobi2Copy berada paga baris 91 yang dimana itu diatas code untuk menghapus data hobi pada baris 95
print(hobi2Copy)

print("\n")
# Sets
# Sets hampir mirip dengna Tuples, bedanya tidak terutut dan bisa di ubah tidak seperti Tuples
# Hampir sama juga seperti dictionary, tetapi tidak memiliki keys value seperti dictionary
# Sets juga bisa tidak dirubah, dengan cara Frozen sets
set1 = {"Rangga", "Putra"}
set2 = {"Rangga"}

intersect = set1 & set2
# Code diatas berfungsi untuk intersect antara set1 dan set2
print(intersect)

print("\n")
set3 = {"Pratama"}
mod = set1 | set3
# Code diatas akan menjadikan 2 set menjadi 1, tetapi bila ada data yang sama dalam kedua set, maka hanya akan ditampilkan 1 saja
print(mod)

print("\n")
# Kita juga bisa mengurangi data antar sets, seperti contoh berikut:
minus = set1 - set2
print(minus)

print("\n")
# Kita juga bisa mengetahui apakah suatu set itu adalah superset(memiliki semua data yang ada dalam set lainnya)
# atau subset(tidak memiliki semua data dalam set lainnya), seperti contoh diwabah:
perbandingan = set1 < set2
# Bila kita menuliskan code diatas, maka hasilnya adalah False, karena set2 tidak memiliki semua data yang ada di set1
# Tapi bila kita menuliskan code seperti dibawah, maka hasilnya adalah True, karena set1 memiliki semua data dalam set2
perbandingan2 = set1 > set2

print(perbandingan)
print(perbandingan2)

print("\n")
# Kita juga bisa menampilkan list dari set, seperti berikut:
print(list(set1))
# Kita juga bisa mengecek apakah ada data yang kita ingin ketahui di dalam set tertentu menggunakan in Operator, seperti berikut:
print("Putra" in set1)

# Sets tidak bisa memiliki 2 data yang sama persis, walaupun dideklarasikan dalam 1 set, tapi bila di tampilkan, maka hanya akan muncul 1
# Salah satu keuntungan set, karena mencegah data redundan / sama
