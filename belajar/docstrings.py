"""_Dog Module_

    This module does bla bla bla and provides the following classes:
    - Dog
    ...
"""
# Docstrings juga biasa di tulis di baris paling atas seperti di atas
# Docstrings
# Dokumentasi sangatlah penting tidak hanya untuk berkomunikasi dengan orang lain
# agar kita lebih mudah memahami code satu sama lain (inti dari function, class, method, atau module dari code yang dibuat)
# Tapi juga untuk diri sendiri, karena bila kita kembali ke code kita setelah beberapa bulan,
# kita mungkin tidak ingat akan beberapa hal bila tidak kita dokumentasikan
# Kita bisa menggunakan 2 cara untuk mendokumentasikan code kita, dengan menggunakan comment, dan docstrings


# Berikut adalah contoh docstrings
def increment(n):
    # code baris ke 12 ini merupakan docstrings
    """Increment a number"""
    return n + 1


class Dog:
    """A Class representing a Dog"""

    def __init__(self, name, age):
        """Initialize a new Dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the Dog Bark"""
        print("Woof!")


print(help(Dog))

# Selain help method diatas, ada banyak method yang bisa digunakan
# untuk mengambil informasi dari code yang kita buat
