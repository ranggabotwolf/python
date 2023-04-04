# Dibawah ini adalah contoh kegunaan operator aritmatik : +-*/%=**//
print("Dibawah ini adalah contoh kegunaan operator aritmatik")
age = 10
age += 10
print(age)
# Diatas adalah age = age + 10, jadi age = 10 + 10 = 20

# Dibawah ini adalah contoh kegunaan operator perbandingan / comparison : == != >< >= <=
print("Dibawah ini adalah contoh kegunaan operator perbandingan / comparison")
a = 1
b = 2

c = a == b
d = a != b
e = a > b
f = a <= b
print(c)
print(d)
print(e)
print(f)


# Dibawah adalah contoh kegunaan operator boolean : not, and, or, nor
print("Dibawah adalah contoh kegunaan operator boolean")
condition1 = True
condition2 = False

# operator "not" dibawah, akan memanggil / mengecek nilai yang bukan condition1
print(not condition1)
# operator "and" dibawah, akan mengecek nilai yang ada dalam condition1 dan condition2, dan semuanya harus bernilai benar bila ingin hasil nya benar, tidak boleh salah satunya salah
print(condition1 and condition2)
# operator "or" dibawah, akan mengecek nilai yang ada dalam condition1 dan condition2, dan bila salah satu nilainya bernilai benar, maka hasilnya akan benar juga
print(condition1 or condition2)


# Operator or akan selalu memunculkan nilai benar yang ditemukan pertama kali, bila tidak, maka akan memunculkan nilai terakhir
print("Berikut adalah penjelasan lebih lanjut mengenai operator or")
# Perintah dibawah akan menampilkan 1, karena nilai pertama adalah 0, dan 0 dalam pemrograman bernilai salah / False
print(0 or 1)
# Perintah dibawah akan menampilkan hey, karena nilai pertama adalah False, sementara nilai keduanya adalah hey, maka akan menampilkan hey
print(False or 'hey')
# Perintah dibawah akan menampilkan hi, karena nilai pertama adalah hi, dan itu bukan nilai yang salah / False, maka or akan menampilkan nilai yang pertama yaitu hi
print('hi' or 'hey')
# Perintah dibawah akan menampilkan False, karena nilai pertama adalah [] yang mana itu adalah bernilai kosong, jadi or akan menampilkan False yang merupakan nilai kedua
print([] or False)
# Perintah dibawah akan menampilkan [], karena nilai pertama adalah False, jadi or akan menampilkan nilai selanjutnya yang tidak bernilai False, yaitu []
print(False or [])

# Operator and akan selalu mengecek kebenaran dari nilai variabel yang pertama, dan bila benar, maka akan lanjut mengecek nilai variabel kedua, tapi bila salah, maka akan mengembalikan nilai yang ada pada variabel pertama
print("Berikut adalah penjelasan lebih lanjut tentang operator and")
# Perintah dibawah akan menampilkan 0 (bisa diartikan juga False), karena nilai pertama sudah bernilai 0 / False
print(0 and 1)
# Perintah dibawah juga akan menampilkan 0 (bisa diartikan juga False), karena sama halnya dengan perintah diatasnya, salah 1 nilai dari variabelnya adalah 0, jadi hasil dari perintah dibawah adalah 0
print(1 and 0)
# Perintah dibawah akan menampilkan False, karena nilai dari variabel pertama bernilai False, *ingat aturan operator and!!!
print(False and "hey")
# Perintah dibawah akan menapilkan hey, kenapa? karena nilai pada variabel pertama tidak bernilai False, dan operator and, akan lanjut mengecek nilai variabel selanjutnya apabila nilai variabel sebelumnya bernilai benar / tidak bernilai False
print("Hi" and "hey")
# Perintah dibawah akan menampilkan [], karena nilai dari variabel pertama adalah [] yang merupakan variabel kosong, atau bisa dibilah juga False, jadi hasil yang ditampilkan adalah []
print([] and False)
# Perintah dibawah akan menapilkan False, karena nilai dari variabel pertama adalah False, maka otomatis perintah and akan berhenti dan menampilkan hasil dari variabel pertama / False
print(False and [])

# Bitwise operator : & | ^ ~ << >>
# Bitwise operator merupakan operator yang jarang digunakan
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

# is dan in operator
# is disebut juga dengan identity operator, digunakan untuk membandingkan 2 objek dan returns true bila keduanya merupakan objek yang sama
# in disebut juga dengan membership operator, digunakan untuk menjelaskan bahwa value berada dalam sebuah list, atau sequence yang lain

# Ternary Operator, memungkinkan untuk mendefinisikan dengan cepat sebuah kondisi
# Berikut adalah contoh coding tanpa Ternary Operator


def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# Berikut adalah contoh coding menggunakan Ternary Operator


def is_value(rank):
    return "You're a Champion!" if rank < 3 else "You're a Loser!"
# Ternary operator basically adalah if else dalam satu baris code
