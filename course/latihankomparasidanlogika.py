inputUser = float(
    input(
        "Masukkan angka lebih dari 0,\n kurang dari 5,\n dan lebih dari 8,\n kurang dari 11:"
    )
)

isKurangDari = inputUser > 0 and inputUser < 5
print(" Hasil isKurangDari:", isKurangDari)
isKurangDari2 = inputUser > 8 and inputUser < 11
print(" Hasil isKurangDari2:", isKurangDari2)
isHasil = isKurangDari or isKurangDari2
print("Hasil :", isHasil, "\n")

isKurangDari3 = inputUser < 1
print(" Hasil isKurangDari3:", isKurangDari3)
isKurangDari4 = inputUser > 4 and inputUser < 9
print(" Hasil isKurangDari4:", isKurangDari4)
isKurangDari5 = inputUser > 10
print(" Hasil isKurangDari5:", isKurangDari5)
isHasil2 = isKurangDari3 or isKurangDari4 or isKurangDari5
print("Hasil2 :", isHasil2)
