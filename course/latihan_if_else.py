# Pendeklarasian if adalah seperti berikut

# program sebelumnya
# if kondisi == aksi
# program selanjutnya
#! if nilainya harus berupa bool, jadi True or False

nama = input("Nama anda siapa? ")

# * 1. Program if inline
# if nama == "Rangga": print(f"Kamu Pintar {nama}")
# print(f"Terima kasih {nama}")
# code diatas menggunakan komentar karena tidak bisa menggunakan if inline akibat install extension yang otomatis merapikan source code

# * 2. Program if indentation
if nama == "Rangga":
    print(f"Kamu Pintar {nama}")
    print(f"Teruslah belajar {nama}")
# 2 baris code diatas masih berada dalam if, sedangkan code dibawah sudah diluar if
print(f"Terimakasih banyak {nama}")

# * Else Statement
if nama == "Rangga":
    print(f"Kamu berhasil {nama}")
else:
    print(f"Aaaaahh kamu bukan {nama}")
print(f"Thanks {nama}")
