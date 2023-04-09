# list compression
# adalah cara membuat list dengan sangat ringkas / cepat

numbers = [1, 2, 3, 4, 5, 6]

# Kita akan membuat list baru, yang tersusun dari list numbers dan di pangkat 2 seperti dibawah :
numbers_pangkat_2 = [n**2 for n in numbers]
# code diatas adalah list compression syntax
print(numbers_pangkat_2)
# hasil dari code diatas adalah list numbers di pangkatkan 2
# menjadi [1, 4, 9, 16, 25, 36]

# list compression terkadang lebih disarankan dibanding loops
# karena lebih mudah di baca ketika perintahnya bisa dituliskan dalam 1 baris code

# berikut adalah contoh bila menggunakan loops
numbers_pangkat_3 = []
for n in numbers:
    numbers_pangkat_3.append(n**3)
print(numbers_pangkat_3)
# bila menggunakan loops akan memakan baris code yang cukup panjang, yaitu 4 baris
# sementara menggunakan list compression hanya 2 baris

# kita juga bisa menggunakan map, tapi lebih complex, seperti berikut:
numbers_pangkat_4 = list(map(lambda n: n**4, numbers))
print(numbers_pangkat_4)
