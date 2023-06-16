banyak = int(input("Masukkan jumlah segitiga yang ingin dibuat : "))
tinggi_segitiga = int(input("Masukkan jumlah tinggi segitiga yang diinginkan : "))

angka = 1
while True:
    angka += 1
    for angka in range(banyak):
        print("*" * angka)
        angka += 1
        tinggi_segitiga -= 1
        if angka >= tinggi_segitiga:
            # continue
            # else:
            break

print(f"Diatas adalah segitiga dengan tinggi {tinggi_segitiga} \n")
print("Program Selesai")
