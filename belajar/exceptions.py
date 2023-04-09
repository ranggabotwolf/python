"""Exceptions"""

# Sangat penting mempunyai cara untuk mengatasi error
# dan Python mempunyai exceptions untuk melakukan itu

# exception handling, caranya kita meletakkan baris code ke dalam try block dibawah
# try:
# beberapa baris code
# dan ketika error terjadi, python akan memberitahu kita error apa yang terjadi menggunakan except block dibawah
# except <ERROR1>:
# Handler <ERROR1>
# bila error2 yang terjadi, maka except handler dibawah yang akan muncul
# except <ERROR2>:
# Handler <ERROR2>
# Kita juga bisa menangkap semua exception menggunakan except tanpa error type seperti dibawah :
# except:
# code diatas akan menghandle exception yang lainnya

# Kita juga bisa menambahkan else block di akhir yang akan berfungsi / berjalan
# jika tidak ada exception ditemukan dalam baris code
# else:
# no exceptions were raised, the code ran succesfully
# Jadi, jika tidak ada error ditemukan dalam baris code dibawah try block
# program akan menjalankan code yang ada dibawah else

# finally:
# do something in any case
# Setiap finally block akan selalu berjalan diakhir code
# tanpa menghiraukan ada atau tidaknya exceptions pada baris code di try block

# result = 2 / 0
# print(result)
# code diatas akan error, karena bilangan 2 dibagi dengan 0 itu tidak bisa
# maka akan muncul ZeroDivisionError
# bila dalam suatu file ditemukan error,
# biasanya program akan berhenti & baris code dibawahnya tidak akan di tampilkan

# Kita akan coba memasukkan code diatas kedalam try block
try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by Zero!")
finally:
    result = 1

print(result)
# Hasil dari code diatas adalah Cannot divide by Zero!, lalu dibawahnya akan tampil 1
# try block memungkinkan program kita akan tetapi berjalan
# walaupun ditemukan error dalam baris code tertentu di try block

print("\n")
# raise Exception('An Error!')
# code diatas akan menampilkan error
# raises a general exception

try:
    raise Exception("An Error!")
except Exception as error:
    print(error)
# alih-alih program error dan tulisan merah bila kita menuliskan code seperti baris ke 51
# kita bisa menggunakan try block, dan akan menampilkan tulisan An Error! dan program tetap berjalan

print("\n")
# Kita juga bisa mendefinisikan exception class milik kita sendiri,
# dan menambahkan Exception di akhir nya, seperti berikut :


class DogNotFoundException(Exception):
    print("inside")
    pass


# pass diatas berarti nothing / tidak ada
# kita harus menggunakannya ketika kita mendefinisikan class tanpa method didalamnya
# atau function tanpa code didalamnya

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")
# Code diatas akan menampilkan Dog not found! karena kita raise Exception baris 66
#
