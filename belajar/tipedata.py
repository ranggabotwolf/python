# Tipe data dibawah adalah String, karena di deklarasikan didalam tanda petik
name = "hi"
print(isinstance(name, str))

# Tipe data dibawah adalah Integer, karena di deklarasikan dalam bentuk angka
rank = 1
print(isinstance(rank, int))

# Tipe data dibawah adalah Float, karena di deklarasikan dalam bentuk desimal
age = 25.4
print(isinstance(age, float))

# Hasil tipe data dibawah adalah False, karena nilai dalam point tipe datanya adalah int karena bukan desimal, sementara di print, point di cek dalam bentuk float
point = 55
print(isinstance(point, float))

# Hasil tipe data dibawah adalah True, karena walaupun nilai dalam point2 sebenarnya adalah int, tetapi nilai nya sudah di convert kedalam tipe data float
point2 = float(56)
print(isinstance(point2, float))

# Hasil tipe data dibawah adalah True, karena "hasil" memanggil nilai yang ada dalam point3 yang akan di convert menjadi int di dalam "hasil"
point3 = "57"
hasil = int(point3)
print(isinstance(hasil, int))
