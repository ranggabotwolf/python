# functions

def hello():
    print('Hello, Rangga!')


hello()
hello()
hello()
hello()
hello()
# Code diatas akan menampilkan Hello, Rangga sebanyak perintah yang dituliskan

# Berikut adalah code yang lebih advanced, code berikut akan menampilkan nama dari hasil yang diketikkan oleh user / pengguna

print("\n")


def halo(nama=input("Siapa nama anda? ")):
    print('Halo, ' + nama)


# hello('Rangga')
halo()


print("\n")


# Kita juga bisa menambahkan parameter baru dalam code hi() dibawah, menjadi hi(jeneng)
# Dimana jeneng akan menjadi variabel yang bisa ditambahkan / digunakan secara fleksibel seperti contoh dibawah:
def hi(jeneng="Kawan"):
    # Code diatas, value Kawan di dalam parameter jeneng akan menjadi isi default yang akan dipanggil otomatis bila pada perintah kita tidak memanggil variabel / memasukkan nilai
    print('Hi, ' + jeneng)


hi("Putra")
hi("Pratama")
# Seperti code dibawah, function hi() dipanggil tanpa mendeklarasikan parameter / variabel didalamnya
# Maka isi default yang akan tampil adalah yang ada di dalam parameter jeneng yang ada di baris code 19
hi()

print("\n")
# Kita juga bisa menambahkan 2 parameter pada suatu fungsi, seperti contoh berikut:


def hai(asmi=input("Siapa nama kamu? "), umur=input("Berapa umur kamu? ")):

    print("Hai " + asmi + ", You're " + str(umur) + " years old!")


hai("Rangga", '25')
hai()


print("\n")
