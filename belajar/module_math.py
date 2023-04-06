# Berikut adalah contoh module math yang kita import
# Dengan mengimport library math, kita bisa menggunakan semua function didalamnya
import math

# Kita juga bisa mengganti code diatas menggunakan
# from math import sqrt
# Dengan code bari ke 5 diatas, kita hanya akan bisa menggunakan function sqrt
# dari library math, tidak bisa menggunakan function lainnya dalam library math

print(math.sqrt(4))
# Tapi jika kita menggunakan code baris ke 5, maka code print diatas akan berubah :
# print(sqrt(4)), kenapa tidak math.sqrt lagi?
# Karena import baris ke 5 sudah menerangkan bahwa import sqrt dari math
# Jadi otomatis bila kita menggunakan function sqrt itu adalah milik lib math
