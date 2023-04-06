# Python menyediakan package lainnya di library standard untuk membantu kita
# yang disebut argparse
import argparse

parser = argparse.ArgumentParser(description="This program prints the name of Hero")

parser.add_argument(
    "-c", "--color", metavar="color", required=True, help="The color to search for"
)
# Penjelasan dari code diatas adalah
# Kita akan menerima c option atau bisa jadi -c atau --color,
# dan kita akan menyimpan / memanggilnya color dengan metavar="color"
# dan nantinya kita bisa melakukan parser.parse_args() seperti code dibawah
# dan lalu kita bisa mengakses arg.color untuk mendapatkan color yang tampil dengan code baris 18
# Kita juga bisa menspesifikasikan require dan help apa yang akan dilakukan di code baris ke 8
args = parser.parse_args()

print(args.color)

# Berikut adalah contoh kita run file ini :
# kita menuliskan code seperti ini
# python [lokasi_file/nama_file] -c blue
# maka yang akan tampil adalah blue
# Karena program diatas mencari warna seperti yang sudah di tuliskan pada code baris 7

# Bila kita menuliskan python [lokasi_file/nama_file] (tanpa -c warna)
# Maka akan muncul tulisan begini :
# usage: nama_file [-h] -c color
# nama_file: error: the following arguments are required: -c/--color
# Error tersebut terjadi karena kita tidak mendeklarasikan / menginputkan warna dalam shell

# Kita juga bisa menambahkan option pada code baris ke 8, setelah required
# contoh, bila kita menambahkan choices={'blue', 'yellow'}
# maka hanya 2 warna, yaitu blue atau yellow yang akan dideteksi / yang bisa ditampilkan
# selain 2 pilihan warna itu, maka akan tampil error seperti baris ke 30
# dengan tambahan invalid choices: warna yang salah (choose from 'blue', 'yellow')

# Menggunakan argparse membuat kita lebih mudah "to deal with arguments"
# dan lebih memudahkan kita "communicate information back" ke user tentang apa yang coba kita ingin dapatkan
