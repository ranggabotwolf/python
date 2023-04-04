from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)
# Perintah diatas akan menampilkan State.ACTIVE
# Sementara perintah dibawah akan menampilkan isi dari State.ACTIVE
print(State.ACTIVE.value)
# Bila ingin menampilkan State.INACTIVE, kita bisa memanggil nilai didalam INACTIVE, seperti contoh dibawah:
print(State(0))
# Bisa juga seperti berikut:
print(State['ACTIVE'])
# Cara ini basically adalah satu-satunya cara membuat constants di dalam Python
print(State['INACTIVE'].value)
# Perintah diatas sama dengan baris ke 12

# Python tidak memaksa setiap variabel adalah constant, jadi beberapa orang menggunakan enum untuk membuat constant
# enum memungkinkan nilai didalamnya tidak bisa di reassign
print(list(State))
# Perintah diatas akan menampilkan list / daftar enaum yang ada dalam class State
print(len(State))
# Perintah diawas akan menampilkan jumlah enum dari State
