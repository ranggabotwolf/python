banyak = int(input("Masukkan jumlah segitiga yang ingin dibuat : "))
tinggi_segitiga = int(input("Masukkan jumlah tinggi segitiga yang diinginkan : "))

angka = 0
count = banyak
while True:
    # many += 1
    count -= 1
    for angka in range(tinggi_segitiga):
        print("*" * angka)
        angka += 1
        if angka == tinggi_segitiga:
            print(f"Ini segitiga nomor {count+1}")
        # continue
    if angka > tinggi_segitiga:
        break
    # break
    if count == 0:
        break
    tinggi_segitiga -= 1
print(f"Diatas adalah segitiga dengan tinggi {tinggi_segitiga} \n")
print("Program Selesai")
