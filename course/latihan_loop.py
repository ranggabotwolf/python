# Perulangan (loop)

# for kondisi
# aksi


# looping data dalam list
angka_list = [0, 3, 9, 5]
print(angka_list)

for i in angka_list:
    print(f"i sekarang -> {i}")
print("Ini adalah akhir dari program 1\n")

# looping data dengan range
angka_range = range(7)
print(angka_range)
for i in angka_range:
    print(f"i sekarang -> {i}")
print("Ini adalah akhir dari program 2\n")

# looping angka dalam range dengan menentukan angka awalnya
angka_range = range(3, 9)
print(angka_range)
# hasil yang akan tampil dari rang ediatas adalah 3,4,5,6,7,8
# karena di awal di set dimulai dari 3
for i in angka_range:
    print(f"i sekarang -> {i}")
print("Ini adalah akhir dari program 3\n")

# looping menggunakan string
data_str = "Rangga Putra Pratama"

for letter in data_str:
    # letter bisa diganti dengan i atau dengan apapun selama itu huruf
    print(letter)
print("Ini adalah akhir dari program 4")
