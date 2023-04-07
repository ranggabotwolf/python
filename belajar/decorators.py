# Decorator


def logtime(func):
    def wrapper():
        # do something before
        print("before")
        val = func()
        # do something after
        print("after")
        return val

    return wrapper


# code baris ke 16 ini adalah decorator
@logtime
# decorator ditandai dengan @ sebelum nama decoratornya
def hello():
    print("hello")


hello()

# Kita biasanya menggunakan decorator untuk mengubah kebiasaan function
# tanpa memodifikasi function itu sendiri
# Contohnya ketika kita ingin menambahkan logging test performance,
# perform caching, verify permissions, dan lainnya
# Kita juga bisa menggunakannya ketika kita perlu menjalankan code yang sama di multiple function
