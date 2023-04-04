def change(nilai):
    nilai["nama"] = "Putra Pratama"
# Perintah diatas akan mengganti dictionary nama : Rangga menjadi Putra Pratama karena dictionary datanya bisa diganti


nil = {"nama": "Rangga"}
change(nil)
print(nil)


def hello(name):
    print('Hello, ' + name + '!')
    return name
# Setiap code diatasnya akan berhenti bila diakhiri oleh return


hello('Rangga')


def hai(jeneng):
    # Kita bisa menuliskan code seperti di bawah ini, code dibawah sama keluarannya seperti code diatas, baris ke 11
    if not jeneng:
        return
    print('Hai, ' + jeneng + '!')


hai("Putra")

print('\n')


def halo(asmi):
    print('Halo, ' + asmi + '!')
    return asmi, "Lusiyanti", 1996
# Hasil dari code diatas adalah akan menampilkan 2 tampilan, yaitu code baris ke 38, lalu code baris ke 34
# Kenapa code baris ke 38 tampil lebih dahulu? Karena perintah dari code ke 33 yang menyuruh print code baris ke 38


print(halo("Eka"))
