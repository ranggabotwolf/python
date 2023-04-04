# Nested function
# Function dalam Python bisa berada dalam function lainnya / nested function
# Seperti contoh berikut:
def talk(phrase):
    def say(word):
        print(word)

# Perintah code dibawah adalah untuk memisahkan setiap kata dalam phrase, dan akan menampilkannya satu per satu ke bawah
    words = phrase.split(' ')
    for word in words:
        say(word)
# Ingat, setiap setelah def / function, code dibawahnya harus menjorok kedalam dari def / function seperti contoh dibawah


talk("I'm going to buy a milk!")


# Berikut adalah contoh lain:
def count():
    count = 0

    def increment():
        # Bila ingin mengambil variable yang sudah dideklarasikan dari luar function,
        # Maka cara yang harus dilakukan adalah dengan mendeklarasikannya sebagai nonlocal, seperti berikut:
        nonlocal count
        count = count + 1
# Code diatas adalah untuk mengambil data dari variable count, yaitu 0, lalu di tambahkan dengan 1
# Maka ketika di print dengan code dibawah, hasilnya adalah 1
        print(count)
# Ingat, akhir setiap function adalah dengan menuliskan function lagi dibawahnya, seperti code dibawah:
# Dan harus sejajar indentasinya dengan functionnya, dan itu wajib, bila belum di deklarasikan lagi functionnya dibawah
# Maka tandanya function tersebut masih berjalan / belum selesai
    increment()


count()
