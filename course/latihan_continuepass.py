# Control flow terdiri dari:
# Continue, pass, break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0
while angka < 5:
    angka += 1
    if angka == 2:
        print("ini angka ke 2")
    elif angka == 4:
        pass  # baris ini tidak akan dieksekusi / dijalankan
    print(angka)
print("\n")
# diatas merupakan contoh penggunaan pass
# pass biasanya digunakan untuk metode / class yang tidak digunakan tapi tetap dideklarasikan
# maka dari itu tujuan digunakannya pass


# continue

number = 0
while number < 6:
    number += 1
    print(f"now is number -> {number}")  # aksi 1
    if number == 3:
        print("Keren")
    elif number == 5:
        print("Mantap")
        continue
    print(f"nomor {number} berhasil di cek")  # aksi 2
    # apapun yang berada dibawah continue akan diskip bila sudah sesuai kondisi code di atas continue nya
    # seperti pada contoh di atas, aksi 2 di skip setelah number = 5
print(f"Selesai {number} kali loop")
