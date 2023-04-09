# with statement sangat membantu menyederhanakan bekerja dengan exception handling
# contohnya ketika bekerja dengan file, setiap kita membuka suatu file
# kita harus ingat untuk menutupnya kembali
# dengan with membuat prosesnya lebih transparan
# berikut adalah contoh tanpa menggunakan with statement

# filename = "users/flavio/test.txt"

# try:
# open file
# file = open(filename, "r")
# read file
# content = file.read()
# print file
# print(content)
# finally:
# close file
# file.close()

# alih-alih menggunakan code diatas, kita bisa menggunakan code dibawah dengan with statement
filename = "/Users/flavio/test.txt"

with open(filename, "r") as file:
    content = file.read()
    print(content)
# dengan code with diatas, akan memastikan bahwa file yang dibuka akan otomatis ditutup diakhir
# dengan kata lain, kita mempunyai built-in implicit exception handling yang akan menutup otomatis
