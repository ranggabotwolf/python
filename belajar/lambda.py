# Lambda functions
# Lambda functions atau dikenal juga anonymous functions
# adalah functions kecil, mereka tidak mempunyai nama
# dan hanya mempunyai 1 expression sebagai body nya
# jadi mereka didefinisikan menggunakan lambda keyword

lambda num: num * 2
# num : adalah contoh arguments lambda functions
# num * 2 adalah expressions
# body nya pasti hanya mempunyai 1 expression, bukan statement

# Perbedaan antara expression dan statement:
# expression return a value
# sementara statement tidak

# Contoh code baris ke 7 adalah lambda function yang berfungsi untuk menyimpan value yang di kalikan 2
# lambda function dapat menerima argumen lebih, seperti contoh berikut :

lambda a, b: a * b
# lambda function tidak dapat dipanggil secara langsung
# tapi kita bisa menetapkan mereka ke variable, seperti contoh berikut :
multiply = lambda c, d: c * d
# lalu kita print seperi code dibawah :
print(multiply(2, 4))
# maka akan menghasilkan nilai 8, karena 2 * 4 adalah 8


# Kegunaan dari lambda functions baru terlihat ketika digabungkan dengan function python lainnya
# Contohnya bila digabungkan dengan map(), filter(), reduce()
