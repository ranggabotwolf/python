# Polymorphism
# polymorphism generalizes a functionality, jadi dapat bekerja pada type yang berbeda
# polymorphism adalah konsep penting dalam object oriented programming


class Dog:
    def eat(self):
        print("Eating dog food")


class Cat:
    def eat(self):
        print("Eating cat food")


# diatas kita mendefinisikan method yang sama (yaitu eat), dalam class yang berbeda
# lalu kita dapat generate object dan kita bisa memanggil eat method
# tanpa menghiraukan dari class mana dia berasal
# dan akan menampilkan hasil yang berbeda

animal1 = Dog()
animal2 = Cat()
# kita mendefinisikan 2 object diatas, Dog() dan Cat() sebagai animal1 dan animal2

animal1.eat()
animal2.eat()
# lalu kita menjalankan method kepada kedua object diatas
