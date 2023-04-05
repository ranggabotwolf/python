# Memoization
from functools import wraps
import kelas
from function import hello


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
