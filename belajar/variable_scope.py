# Functions
age = 8
# Jika mendeklarasikan variable diluar function seperti variable diatas,
# maka variable tersebut dapat digunakan untuk semua hal dibawah variable tersebut, termasuk function dibawahnya
# Nama lain dari variable tersebut adalah Global Variables


def test():
    print(age)


print(age)
test()

# Tapi jika kita mendeklarasikan variable di dalam function, maka variable itu tidak bisa digunakan di luar dari function tersebut
# Nama lain dari variable tersebut adalah local variable, Seperti contoh berikut :


def coba():
    umur = 9
    print(umur)


# Code perintah print dibawah error, karena code itu berada diluar code def coba() baris ke 19 (*ingat, indentasi di python sangat berpengaruh)
# Code dibawah error karena variable umur tidak terdefinisi, karena perintah dibawah sudah diluar indentasi code baris ke 19
print(umur)
coba()
