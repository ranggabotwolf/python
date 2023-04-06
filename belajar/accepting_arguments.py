# Accepting Arguments
import sys

print(sys.argv)

# Berikut adalah contoh Accepting Arguments
# Jadi ketika kita menjalankan file ini kedalam shell dengan menuliskan seperti ini :
# python [lokasi_file/nama_file] yang ingin kita tampilkan, contoh Rangga
# Maka program yang akan tampil adalah ['lokasi_file/nama_file', 'Rangga']
# Semua berada dalam string

# Kita juga bisa membuat perintah seperti ini
name = sys.argv[1]
# Code diatas akan mengambil system argumen index ke 1
# Dan akan di tampilkan dengan code dibawah
print(f"Hello {name}")
# Jadi bila kita menuliskan python [lokasi_file/nama_file] Rangga 25 pada shell
# Maka yang akan tampil adalah Hello Rangga, karena Rangga berada pada index 1 pada shell
