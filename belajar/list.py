# List adalah data structure dalam Python
# Seperti contoh berikut:
everything = ["dragon", 4, "ryu", True, 3.6]
# List seperti diatas, bisa & boleh mengandung lebih dari 1 tipe data
print("dragon" in everything)
# Perintah diatas merupakan in Operator, yang berfungsi untuk mengecek apakah data yang di inginkan berada pada list / variable yang diinginkan
print("Rangga" in everything)
# Perintah diatas akan menampilkan False, karena Rangga tidak ada di dalam list / variable yang dipanggil
# list juga bisa tidak diisi / kosong, caranya adalah dengan hanya mendeklarasikan [] saja, seperti everything = []
# Kita juga bisa menampilkan data di dalam list sesuai index yang kita inginkan, seperti contoh berikut:
print(everything[2])
# Perintah diatas akan menampilkan ryu, karena ryu adalah index ke-2 dari list everything

# Kita juga bisa mengupdate data di dalam list, dengan acuan index berapa yang ingin kita update datanya
# Contoh seperti dibawah
print(everything)
# Perintah diatas akan menampilkan list lama yang ada pada everything
everything[1] = "Naga"
# Code diatas akan mengganti list index ke-1 dari everything, yaitu 4, menjadi Naga
print(everything)
# Code diatas akan mencetak list everything yang baru, dengan list index ke-1 yang telah terganti dari yang sebelumnya bernilai 4, menjadi Naga

# Seperti pada file string, kita bisa mencetak list menggunakan index -(minus), seperti contoh berikut:
print(everything[-4])
# Code diatas akan menampilkan list everything dengan index ke- (-4), yaitu Naga
print(everything[1:4])
# Code diatas akan menampilkan list everything dari index ke-1 sampai index ke sebelum 4, yaitu 3
print(len(everything))
# Code diatas akan menampilkan jumlah list yang ada di dalam everything
# Kita juga bisa menambahkan data di dalam list dengan append function, seperti berikut:
print("\n")
print(everything)
print(len(everything))
everything.append("Rangga Putra Pratama")
# Code diatas berfungsi untuk menambahkan data dalam list
print(everything)
print(len(everything))
# Dan setelah di print, ternyata data Rangga Putra Pratama telah berada dalam list everything

print("\n")
# Bila ingin menambahkan lebih dari satu data di dalam list, maka selain append, bisa gunakan extend
everything.extend(["Love", "Eka Lusiyanti"])
# Code diatas berfungsi menambahkan lebih dari 1 data dalam list
print(everything)
# Selain extend, += sama dengan extend fungsinya, lihat contoh berikut:
everything += ["Last", "Forever"]
# Code diatas sama fungsinya dengan extend
print(everything)
# Ketika menggunakan extend atau +=, jangan lupa [] pada data yang akan ditambahkan, bila tidak, maka setiap karakter akan terpisah, dan dianggap sebagai 1 data
# Seperti contoh berikut:
everything += "LOVE"
print(everything)
# silahkan lihat sendiri, kata LOVE yang ditambahkan akan terpisah masing-masing karakternya, menjadi data tersendiri karena lupa menggunakan [] di luarnya

print("\n")
# Kita juga bisa menghapus data yang ada dalam list, seperti contoh berikut:
everything.remove(3.6)
# Code diatas menghapus data 3.6 dari list
print(everything)

print("\n")
# Kita juga bisa menghapus data yang terakhir ditambahkan menggunakan pop(), seperti contoh berikut:
print(everything.pop())
# Code diatas menghapus data yang terakhir ditambahkan, yaitu E dari LOVE (yang sebelumnya lupa menambahkan [], agar tiap karakternya tidak terpisah)
print(everything)

print("\n")
# Kita juga bisa menambahkan data kedalam list, bahkan ke index / posisi yang kita inginkan, seperti contoh berikut:
everything.insert(3, "Champion")
print(everything)

print("\n")
# Kita juga bisa memotong beberapa data dalam list dengan menggantinya sekaligus dengan data yang baru (menurut index), seperti contoh dibawah:
everything[2:2] = ["Tes1", "Tes2"]
# Code diatas akan memotong index 2, dan menyisipkan Tes1, dan Tes 2 ke index 2, dan data pada index 2 sebelumnya akan bergeser setelah data yang baru dimasukkan
print(everything)

print("\n")
# Sementara code dibawah akan memotong index 2 sampai index sebelum 5, yaitu 4, dan menggantinya dengan data Baru1, dan Baru2
# Jadi data yang akan hilang dari data dalam list sebelumnya adalah Tes1, Tes2, dan ryu
everything[2:5] = ["Baru1", "Baru2"]
print(everything)


print("\n")
# Sorting Lists
# Sorting list hanya bisa dilakukan bila tipe data dalam list 1 tipe semua, seperti contoh dibawah:
sorting = ["Putra", "Rangga", "Pratama", "Eka", "lusiyanti"]
# Kelemahan dari code diatas, huruf pertama kapital dan tidak, akan dibedakan urutannya, dan dimulai dari huruf pertama yang kapital
sorting.sort()
print(sorting)

print("\n")
# Code dibawah berfungsi untuk mengcopy data yang ada di list sorting, kita juga bisa memilih index mana yang akan ditampilkan (bila kita mengisi bagian [:])
sortingcopy = sorting[:]
sorting.sort(key=str.lower)
# Sementara code diatas, tidak akan memisahkan antara huruf awal kapital atau tidak, semuanya akan diurutkan sesuai ABJAD
print(sorting)
print(sortingcopy)
# Walaupun code print(sortingcopy) berada dibawah code print(sorting), tetapi data yang tampil, di urutkan secara terpisah antara
# data huruf awalnya kapital dan yang tidak, mengapa? karena code sorting pada baris 95 berada 1 baris diatas sorting.sort(key=str.lower)
# yang berfungsi untuk tidak memisahkan antara data yang huruf awalnya kapital dan yang tidak ketika ditampilkan & sudah diurutkan

print("\n")
# Kita juga bisa menyederhanakan perintah diatas menjadi 1 baris code, seperti berikut:
print(sorted(sorting, key=str.lower))
# Hasil yang akan ditampilkan code diatas, sama saja dengan code pada baris ke 96
