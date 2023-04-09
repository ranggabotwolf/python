# Operator Overloading
# adalah teknik lanjut yang bisa kita gunakan untuk membuat classes comparable
# dan membuat mereka bekerja dengan python operator


class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # baris code dibawah merupakan operator overloading
    # __gt__ artinya greater than / lebih besar dari
    def __gt__(self, other):
        return True if self.age > other.age else False


roger = Dog("Roger", 9)
syd = Dog("Syd", 7)
rusle = Dog("Rusle", 10)

print(roger > syd)
# perintah diatas akan menampilkan True, karena age roger > syd
# sementara perintah dibawah akan menampilkan False, karena age roger < rusle
print(roger > rusle)

# __gt__ pada code baris ke 14 yang berarti greater than
# kita bisa menggantinya dengan yang lain, seperti kurang dari, lebih dari samadengan, dll
# dibawah adalah list yang bisa digunakan selain __gt__ dan operator >
# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator
