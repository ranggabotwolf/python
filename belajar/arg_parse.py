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
