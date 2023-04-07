# Recursion
# function dalam python dapat memanggil dirinya sendiri, yang demikian disebut recursion

# Contoh faktorial
# 3! = 3 * 2 * 1 = 6
# 2! = 2 * 1 = 2


# Menggunakan recursion, kita bisa menuliskan function yang menghitung faktorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# diatas adalah function dalam function memanggil function yang sama
# recursive function selalu mempunyai base case (baris ke 11-12), dan recursive case (baris ke 13)
# base case adalah ketika program keluar dari recursive function
# Kita harus membuat base case jadi functionnya bisa berhenti
# bila kita tidak membuat base case nya, maka yang akan terjadi adalah infinite / error
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))

