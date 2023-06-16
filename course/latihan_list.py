# LIST

# * 1. Kumpulan data numbers
data_angka = [1, 5, 2]
print(data_angka)
print("Diatas adalah contoh list angka\n")


# * 2. Kumpulan data string
data_string = ["rangga", "putra", "pratama"]
print(data_string)
print("Diatas adalah contoh list string\n")

# * 3. Kumpulan data boolean
data_bool = [True, False, False, True]
print(data_bool)
print("Diatas adalah contoh list boolean\n")

# * 4. Kumpulan data campuran
data_mix = [4, "rama", "10", True, "Lusi", False, 99]
print(data_mix)
print("Diatas adalah contoh list campuran int, string, bool\n")


# * Cara alternatif membuat list
data_range = range(1, 10)
# bila ingin membuat range dari 0 sampai sebelum 10
# maka cukup tuliskan 10 saja di dalam range
# karena by default number / int dimulai dari 0
print(data_range)
print(
    "Diatas adalah contoh cara alternatif membuat list dengan range, tapi tidak tampil data satu per satu\n"
)
# code baris ke 22 diatas tidak akan menampilkan data range dari 1, 2, 3, 4 sampai 9
# tapi range (1, 10)
# tapi bila kita masukkan data_range diatas kedalam list,
# maka baru akan tampil 1, 2, 3, sampai 9
data_list = list(data_range)
print(data_list)
print(
    "Diatas adalah contoh cara alternatif membuat list dengan range dengan tampil secara list\n"
)
# code dibawah akan menampilkan range dari 0 sampai 9 dengan kelipatan angka (increment) 2
# jadi yang akan tampil adalah 0, 2, 4, 6, 8
# karena angka 2 dibelakang digunakan untuk increment
data_list2 = list(range(0, 10, 2))  # range(start, stop, step)
print(data_list2)
print("Diatas adalah contoh membuat list dengan increment 2\n")

# * Membuat list dengan for loop, list comprehension
list_pake_for = [i for i in range(0, 50, 5)]
print(list_pake_for)
print("Diatas adalah contoh membuat list dengan for loop\n")

# fungsi list dengan for loop adalah agar kita
# bisa membuat operasi tambahan dalam list seperti berikut
list_pake_for = [i**2 for i in range(10)]
# hasil dari code diatas adalah semua angka dalam list
# akan di pangkatkan 2
print(list_pake_for)
print("Diatas adalah contoh membuat list dengan for loop dan kelipatan 2\n")

# * Membuat list pake for if
list_pake_for_if = [i for i in range(20) if i not in [5, 10, 15]]
print(list_pake_for_if)
print("Diatas adalah contoh membuat list dengan for if\n")
# Membuat list bilangan genap
# dengan cara menambahkan i % 2 == 0
# yang artinya bila i modulus 2 = 0 (i dibagi 2 sisa hasilnya 0)
# maka angka itu yang akan ditampilkan
list_pake_for_if = [i for i in range(25) if i % 2 == 0 and i not in [5, 10, 15]]
print(list_pake_for_if)
print(
    "Diatas adalah contoh membuat list dengan for if dan tampil bilangan genap & tidak ada di list [5,10,15]\n"
)

list_pake_for_if = [i for i in range(25) if i % 2 != 0 and i not in [5, 10, 15]]
# code diatas akan menampilkan list angka dengan bilangan ganjil
print(list_pake_for_if)
print(
    "Diatas adalah contoh membuat list dengan for if dan tampil bilangan ganjil & tidak ada di list [5,10,15]\n"
)
