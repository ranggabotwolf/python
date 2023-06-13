# true bisa digunakan juga menjadi kondisi dalam looping
# dan akan mengacu kepada kondisi yang terakhir
# seperti contoh dibawah

data_int = int(input("Hitung sampai = "))
cari = int(input("Bilangan yang ingin dicari adalah angka = "))

angka = 0

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == cari:
        print(f"{cari} sudah ketemu")
        break
    if angka == data_int:
        print(f"Maaf, angka {cari} tidak ketemu")
        break
    else:
        print(f"Mohon bersabar, program sedang mencari angka {cari}")

print("Program telah berhenti")
