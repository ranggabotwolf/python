# Ada satu lagi tipe data selain int dan float, yaitu complex
# Complex adalah ekstensi dari familiar real number system, dan number itu terdiri dari penjumlahan dari real number part & imaginary number part
# imaginary number adalah i dalam matematika atau j dalam teknik, contoh : 3 + 4j, 3 adalah real number part 4j adalah imaginary number part
num1 = 2+3j
num2 = complex(2, 3)

print(num2.real, num2.imag)
# Perintah diatas akan menghasilkan 2.0 dan 3.0, yang mana 2.0 adalah real part dan 3.0 adalah imaginary part, dan semua dalam float
print(type(num2.real), type(num2.imag))
# Dan setelah di cek oleh perintah diatas, Benar, bahwa tipe data dari num2.real dan num2.imag adalah float

print("\n")
# Berikut adalah sesi Built-in function
# abs adalah salah satu dari Built-in function, yang mana berfungsi untuk mengembalikan nilai absolute dari bilangan / number
# Contoh seperti berikut
print(abs(5.5))
# Perintah diatas akan menampilkan 5.5
print(abs(-6.5))
# Perintah diatas akan menampilkan 6.5, padahal dalam abs itu nilainya -6.5, tapi karena function abs, jadi yang ditampilkan adalah nilai absolute nya
print(round(8.7))
# Perintah diatas, round, akan membulatkan nilai yang ada di dalamnya ke bilangan bulat terdekat, >= 0.5 akan dibulatkan keatas
print(round(4.5894, 2))
# Perintah diatas akan menampilkan 2 angka dibelakang koma, dan tentu saja dibulatkan ke bilangan bulat terdekat, >= 0.5 akan dibulatkan
