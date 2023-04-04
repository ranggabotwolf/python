done = True
# done = False
# Perlu diingat, huruf kapital awal pada True dan False sangat penting, karena bila huruf awalnya tidak kapital, maka tidak akan dianggap True atau False di Python
# Booleans adalah nilai True atau False pada pemrograman
if done:
    print("Yes")
else:
    print("No")

# String akan selalu benar bila berisi, dan isinya bukan 0, tetapi bila string nya kosong seperti ini : "" atau berisi 0, maka hasilnya False

coba = "Rangga"
# Perintah print dibawah adalah untuk mengecek apakah tipe data dari coba adalah boolean (True or False), dan hasilnya False, karena coba tipe datanya adalah str
print(type(coba) == bool)
# Walaupun perintah print tipe data coba adalah salah (bukan boolean), tapi hasil perintah dibawah ini akan bernilai Benar
# Karena walaupun tipe datanya bukan boolean, tetapi masih ada isinya, jadi tetap bernilai benar, beda cerita bila isinya kosong atau 0, pasti False hasilnya
if coba:
    print("Benar")
else:
    print("Salah")

print("\n")

password = "Qwerty"
print(type(password) == str)
# Perintah dibawah berfungsi untuk mengecek apakah tipe data password adalah str, bila ya, maka print perintah pertama, bila tidak print perintah else
if type(password) == str:
    print(f"Selamat Datang {coba}")
else:
    print("Silahkan Coba Lagi")

# Berikut adalah contoh dari any function
book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
# Perintah di atas akan menampilkan True, karena any function akan bernilai benar selama ada nilai yg benar / True dalam variabel yang di deklarasikan

# Berikut adalah contoh dari all function
ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
# Perintah di atas akan menampilkan False, karena all function akan bernilai benar apabila kedua / variabel yang di panggil semuanya bernilai benar / True
