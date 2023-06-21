data_angka = [1, 3, 2, 3, 1, 5, 2, 1, 6, 1, 1, 6, 7, 1, 4, 6, 2, 7, 8, 9, 1, 0]
print(f"data angka = {data_angka}\n")

# * count data
jumlah_data_1 = data_angka.count(1)
# code diatas digunakan untuk menghitung jumlah suatu data dalam list
# sangat berguna bila yang ingin dicari adalah data dalam list yang berisi sangat banyak data didalamnya
print(f"Jumlah angka 1 dalam list adalah = {jumlah_data_1}\n")

# * ambil posisi data
data = ["Rangga", "Pratama", "Putra", "botWolf"]
print(data)

ambil_data = data.index("Pratama")
print(f"\ndata Pratama berada pada posisi index ke = {ambil_data}")

# * mengurutkan list
print(f"\ndata sebelum diurutkan = {data}")
print(f"\ndata sebelum diurutkan = {data_angka}")
data.sort()
data_angka.sort()
print(f"\ndata sesudah diurutkan = {data}")
print(f"\ndata sesudah diurutkan = {data_angka}")

# * mengurutkan dari data yang terbesar
# ! data harus diurutkan dulu menggunakan sort()
# ! lalu di balik menggunakan reverse()
data.reverse()
data_angka.reverse()
print(f"\ndata sesudah diurutkan dari yang terbesar = {data_angka}")
print(f"\ndata sesudah diurutkan dari yang terbesar = {data}")
