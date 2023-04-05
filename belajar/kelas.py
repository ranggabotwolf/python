# Classes
# Class adalah type dari object
# Sementara object adalah instance dari class

# Berikut adalah contoh class

class Dog:
    def bark(self):
        # self adalah argument dari method yang akan menuju pada object instance yang sedang digunakan saat ini
        # dan harus spesifik dalam mendeklarasikan methodnya
        # Jadi jika kita membuat method dalam class, kita selalu memulainya dengan self
        print('Woof!')


# Berikut adalah contoh dari class, yang mana itu adalah object
roger = Dog()
# Diatas adalah object dari roger yaitu class Dog()
print(type(roger))
# Code diatas untuk melihat type dari roger, dimana type nya adalah class Dog()

# Ada spesial method, yaitu init, yang mana init adalah sebuah constructor
# Berikut ini adalah contoh constructor

print('\n')


class Superhero:
    def country(self):
        print('USA')

# Class Hero inherit dari Superhero class, inherit (warisan)


class Hero(Superhero):
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    # Code diatas adalah salah satu contoh constructor
    # Constructor berfungsi untuk menginisialisasi 1 atau lebih properties ketika kita membuat object baru dari class tersebut
    # name dan ability adalah salah satu properties yang kita tambahkan dalam class Hero

    def team(self):
        print('Avengers')


hulk = Hero('Hulk', 'Super Power')
# Code diatas kita telah membuat Hero
# Dimana nama Hulk ditetapkan sebagai value dari properties name yang berasal dari constructor self.name
# Dan ability Super Power ditetapkan sebagai value dari properties ability yang berasal dari constructor self.ability

print(hulk.ability)
# Contoh code diatas, bila kita menuliskan hulk.ability
# itu adalah self.ability, dan kita sudah mendeklarasikan Super Power sebagai value dari properties self.ability
print(hulk.name)
print(hulk.team())
# Hasil dari code baris ke 48 adalah Avengers, dan dibawahnya akan tampil none, kenapa?
# Karena team() didalamnya sudah ada perintah print, yaitu baris ke 36
# Karena tidak ada return statement dari code baris ke 36, maka dari itu print dari code baris ke 48 adalah Avengers dan dibawahnya adalah none
# Maka dari itu cukup kita panggil hulk.team() tanpa menggunakan print di depannya seperti berikut:
hulk.team()

print('\n')
# * Inheritance
hulk.country()
# ? Code diatas kita bisa memanggil country pada class hulk, kenapa?
# Karena class hulk, yaitu Hero adalah warisan dari class Superhero
# Class Hero sebenarnya tidak memiliki country method, tapi dapat method itu dari class Superhero
