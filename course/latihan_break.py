# break
angka = 0
while angka < 5:
    angka += 1
    print(f"angka sekarang adalah {angka}")

    if angka == 3:
        print(f"angka {angka} ketemu")
        break
    print("keren")
print(f"{angka} kali looping sudah cukup")
