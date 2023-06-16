# latihan loop

# * 1. Loop menggunakan for untuk membuat segitiga
print("ini adalah awal for")
sisi = 10

count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

print(f"Ini adalah hasil for sebanyak {sisi}\n")

# * 2. Loop menggunakan while untuk membuat segitiga
print("ini adalah awal while")
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

print(f"Ini adalah hasil while sebanyak {sisi}\n")

# * 3. hanya ganjil saja
count = 1
while True:
    if count % 2:
        print("*" * count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print("ini adalah akhir dari print ganjil saja")

# * 4. Segitiga sama sisi
count = 1
spasi = sisi // 2
while True:
    if count % 2:
        print(spasi)
        print(" " * spasi, "*" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print("Ini adalah akhir dari program segitiga sama sisi")
