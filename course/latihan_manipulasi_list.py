# Operasi manipulasi list

# semua index berawal dari 0 bila tidak kita set awalnya berapa
# index  0 / (-3)  1 / (-2)  2 / (-1)
data = ["rangga", "pratama", "putra"]
print(data)
# index juga bisa diset dengan -(minus), dan yang akan tampil dimulai dari list paling belakang

# * mengambil data dari list diatas menggunakan index
data1 = data[1]
# code diatas akan mengambil data pada list data dengan index ke 1 yaitu "pratama"
print(f"\ndata yang diambil dari data[1] / index 1 adalah = {data1}")

# bila kita ingin menampilkan data terakhir dalam list
# tetapi tidak tahu index ke berapa data tersebut
# maka menggunakan -(minus) dalam index akan sangat berguna
data_terakhir = data[-1]
print(
    f"\nData berikut adalah data terakhir dalam list yang diambil dari index -1 yaitu = {data_terakhir}"
)


# * Mengambil info jumlah data dalam list adalah menggunakan len
panjang_data = len(data)
print(f"\npanjang data adalah = {panjang_data}")

# * Manipulasi data list

# * 1. Menambahkan item pada list sesuai posisi
print(f"\nData sebelum ditambah adalah = {data}")
# cara untuk menambahkan data pada list di posisi tertentu adalah seperti berikut:
# nama_variable.instert(posisi / index, item)
data.insert(1, "Rama")
print(f"\nData sesudah ditambah adalah = {data}")

# * 2. Menambahkan item pada list di posisi terakhir / di akhir list
# Menggunakan append akan selalu menambahkan item pada list di posisi terakhir
data.append("botWolf")
print(f"\nData ditambahkan menggunakan append adalah = {data}")

# * 3. Menambahkan / menggabungkan 2 list
# Menggunakan extend berfungsi untuk menggabungkan antar list
data_baru = ["Eka", "Lusiyanti"]
data.extend(data_baru)
print(f"\nData digabungkan menggunakan extend adalah = {data}")

# * 4. Merubah data
# Kita ubah data index ke 4 yaitu botWolf menjadi Love
data[4] = "Love"
print(f"\nData setelah diubah index ke 4 adalah = {data}")

# * 5. Meremove / Delete Data
data.remove("Rama")
print(f"\nData setelah dihapus Rama adalah = {data}")
#! Perlu diingat, item yang ingin dihapus caseSensitive

# * 6. Meremove / Delete data paling belakang / posisi terakhir dalam list
data_akhir = data.pop()
print(f"\nData setelah dihapus dengan perintah .pop() adalah = {data}")

# Untuk mengecek data apa yang terakhir dihapus adalah dengan cara seperti berikut :
print(f"\nData berikut adalah item yang dihapus terakhir pada list = {data_akhir}")
