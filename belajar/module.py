# Memoization
from functools import wraps
import kelas

# Perintah dibawah berubah otomatis karena sebelumnya sudah mengimport file function
# Tapi berhubung file function sudah berpindah tempat kedalam folder lib
# Maka code dibawah berubah, bertambah belajar.lib. dimana itu adalah letak foldernya
# Code dibawah juga bisa diganti dengan from lib import function
# Tapi bila kita menggunakan perintah import diatas,
# Maka code baris 38 berubah, bukan hello(), tapi menjadi function.hello()
from belajar.lib.function import hello


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


# Moduls
# Setiap file python adalah module, kita bisa mengimport module dari file apapun

kelas.Superhero()
# Code diatas akan menampilkan apa yang ada pada class Superhero()
# yang ada pada file kelas.py

# Alih-alih menggunakan import seperti import kelas diatas
# Kita bisa menggunakan code seperti dibawah :
hello()
# Code diatas, kita langsung bisa menuliskan methodnya, test()
# Karena sudah kita import menggunakan from nama_file import nama_method() yang ingin di panggil
# Jadi hasil dari code diatas adalah memanggil method yang ada pada file variable_scope


# Dengan membuat file __init__.py pada suatu folder
# Maka itu akan memberitahu python bahwa folder tersebut mempunyai modules
# Dalam kasus ini dalam folder lib, terdapat file function.py
