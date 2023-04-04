# String biasanya di deklarasikan dengan tanda petik "" atau ''
"Ini adalah string"
'Ini juga merupakan string'

Nama = "Rangga"
Nama_lengkap = Nama + " Putra Pratama"
Nama_lengkap += " adalah nama saya"
print(Nama_lengkap)

# Multi-line string bisa digunakan bila mendeklarasikan nilai di dalam tanda petik 3x, contoh seperti di bawah:
print("""Rangga
berusia
25 tahun
""")
# tanda petiknya boleh "" atau '', selama pembuka dan penutupnya sama

print("Rangga Putra Pratama".upper())
# perintah diatas digunakan untuk membuat nilai "Rangga" menjadi huruf besar semua
# Perintah lainnya adalah seperti: isalpha, isalnum, isdecimal, lower, islower, isupper, title, startsswith, endsswith, replace, split, strip, join, find
# Perintah seperti upper, lower, dll diatas, tidak menggantikan nilai asli dari variabel yang dipanggil, tetapi menampilkan hasil nilai yang baru sesuai perintah yang diberikan
# Contoh seperti dibawah ini:
name = "Rangga"
print(name.upper())
# Perintah diatas akan menampilkan "Rangga" dengan huruf besar semua, RANGGA, karena sesuai perintah .upper()
# Sementara perintah dibawah akan menampilkan "Rangga" sesuai dengan yang sudah dideklarasikan sebelumnya, Rangga
# Karena perintah sebelumnya (name.upper()) tidak mengganti nilai dari name, melainkan menampilkan sesuatu yang baru tergantung yang diperintahkan
print(name)
# Perintah dibawah (len()) digunakan untuk menghitung jumlah string yang ada dalam variabel yang disebutkan
print(len(name))
# Perintah dibawah merupakan in Operator, yang telah disebutkan pada bagian Operator sebelumnya
# in Operator digunakan untuk mengecek suatu string mengandung substring yang ingin di cek, seperti contoh dibawah:
# Perintah dibawah mengecek apakah ada substring "gg" pada string name yang berisi "Rangga", dan hasilnya adalah True, karena ada "gg" pada "Rangga"
print("gg" in name)

print("Dibawah adalah contoh penggunaan Escaping Characters")
# Escaping characters
# Agar tanda petik " dapat digunakan / ditampilkan, dan tidak dianggap sebagai string adalah dengan menggunakan Escape characters
# Caranya adalah menggunakan tanda \ sebelum karakter yang akan ditampilkan, contoh seperti dibawah:
bot = "Bot\"Wolf\""
print(bot)
# Tanpa menggunakan tanda \ juga bisa, asalkan tanda petik pembuka dan penutupnya berbeda dengan yang akan disisipkan ditengah, seperti contoh code dibawah
bot2 = 'Bot"Kyle'
print(bot2)
# Bila ingin menampilkan 2 tanda petik yang berbeda seperti contoh dibawah, maka menggunakan tanda \ diwajibkan agar bisa tampil
bot3 = 'Bot"\'Oliver'
print(bot3)

# Bila ingin menampilkan kata di 2 line yang berbeda, gunakan \n di tengahnya, seperti contoh berikut :
hello = "Hi,\nBotWolf"
print(hello)
# Bila ada tanda \ ditengah-tengah string, maka itu adalah Escaping Character
hi = "Bot\\Wolf"
print(hi)

print("\n")
# String Characters & Slicing
# Kita bisa mendapatkan nilai tertentu dalam string, dengan contoh perintah seperti dibawah:
nama = "Rangga Putra Pratama"
print(nama[9])
# Perintah diatas adalah untuk menampilkan nilai index ke-9 dari string yang ada dalam variabel nama, yaitu t
# Bisa juga menggunakan index - (minus), dan bila menggunakan index -, maka -1 adalah nilai terakhir dari string yang deklarasikan
# Seperti contoh berikut, menampilkan nilai index ke-(-2) dari string Rangga Putra Pratama, yang hasilnya adalah m :
print(nama[-2])

# Bisa juga menggunakan range, yang disebut juga slicing, seperti contoh berikut:
print(nama[7:12])
# Perintah diatas adalah menampilkan nilai yang ada mulai dari index ke-7 sampai index sebelum ke-12, jadi nilai index 7-11 yang akan ditampilkan
# Bisa juga menggunakan range kosong di salah satu sisinya, yang menandakan sampai akhir bagian yang kosong tersebut, seperti contoh berikut:
print(nama[:12])
# Perintah diatas berhubung nilai range awalnya kosong, maka akan menampilkan dari index 0 sampai index sebelum 12, yaitu 11
# Sementara perintah dibawah berhubung nilai range akhirnya kosong, maka akan menampilkan dari index 13 sampai akhir nilai stringnya
print(nama[13:])
