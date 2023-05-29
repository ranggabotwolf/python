# Date and Time (Latihan)

import datetime as dt

hari_ini = dt.date.today()

print(hari_ini)
print(f"Hari pada tanggal {hari_ini} adalah hari : {hari_ini:%A}\n")

# Kita juga bisa menginputkan tanggal manual seperti dibawah
tanggal = dt.date(2023, 5, 6)
print(tanggal)
print(f"Hari pada tanggal {tanggal} adalah hari : {tanggal:%A}\n")

# Latihan penghitung umur dari tanggal lahir
print("Silahkan masukkan tanggal,\n bulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari pada tanggal {tanggal_lahir} adalah hari : {tanggal_lahir:%A}\n")

umur_hari = hari_ini - tanggal_lahir
print(f"Umur anda saat ini adalah : {umur_hari}\n")

umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
umur_hari_sisa = (umur_hari.days % 365) % 30
print(
    f"Umur anda saat ini adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan, {umur_hari_sisa} hari\n"
)
