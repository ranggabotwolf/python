# Latihan Kalkulator Sederhana

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operator yang ingin digunakan untuk operasi: ")
hasil = float()

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "/":
    hasil = angka1 / angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "^":
    hasil = angka1 ^ angka2
elif operator == "//":
    hasil = angka1 // angka2
elif operator == "%":
    hasil = angka1 % angka2
else:
    print("Maaf, operasi tidak ada, silahkan coba kembali")
print(f"Hasil dari {angka1}{operator}{angka2}={hasil}")
