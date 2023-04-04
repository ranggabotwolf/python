# Closures
# Closures memungkinkan nested function dapat menggunakan variable diluar nested functionnya
# walaupun function luar tidak aktif lagi
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        # Dibawah ini kita return count didalam nested function
        return count
    # Dan diluar nested function kita return increment
    return increment


# Lalu kita memanggil function counter() dan dimasukkan kedalam variable increment
# Dimana variable increment dibawah adalah return dari increment baris ke 12
increment = counter()
# Kemudian kita print seperti code dibawah,
# Dan karena kita memanggil inner function (increment function), Maka tidak akan mereset nilai count ke 0 lagi setiap di print
# maka nilai variable count pada function counter() akan bertambah 1 setiap di print
# Sesuai dengan perintah baris ke 8
print(increment())
print(increment())
print(increment())
# Jadi kita me-return increment inner function yang mana masih memiliki akses ke variable count pada outer function yaitu counter()
# Walaupun counter function sudah selesai / berakhir
