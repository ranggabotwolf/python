# Loops
# Python mempunyai 2 loops, yaitu for loops dan while loops

# While loops akan selalu berulang sampai kondisi loops nya bernilai salah
condition = True
while condition:
# code iteration / pengulangan diatas akan mengulang code dibawah
# Code iteration / pengulangan diatas akan mengecek kondisi nya bernilai True / False
# Jika benar, maka code iteration diatas akan menampilkan code dibawah (dalam indentasi condition sebelumnya)
   print('The Condition is True')
   condition = False
   
   print('\n')
   
   count = 0
   while count < 10:
   # Dan counter diatas adalah untuk menghentikan loops, yaitu jika nilai count >=10
      print('The Condition is True', count+1)
      count += 1
   print('After the loop')

print('\n')
# For Loops
# For loops biasa digunakan untuk mengulang data yang ada dalam list / mengulang sesuatu nilai
items = [1, 2, 3, 5, 6, 8, 9]
for item in items:
   print(item)

print('\n')
# Kita juga bisa menampilkan / mengulang sesuatu dalam range, seperti berikut;

for nomor in range(8):
   print(nomor)

print('\n')

# Kita juga bisa mengetahui index berapa dalam for loops, seperti berikut:

nomers = [1, 2, "Rangga", 4, 5]
for index, nomer in enumerate(nomers):
   print(index, nomer)

print('\n')

# Break and Continue
# While dan for loops dapat di hentikan / di ganggu di dalam block menggunakan break atau continue
# Continue akan menghentikan iteration / pengulangan yang sedang berjalan
# dan meminta Python untuk melanjutkan pengulangan selanjutnya 
# Sementara break menghentikan semua pengulangan dan melanjutkan perintah selanjutnya setelah pengulangan

datas = [1, 2, 3, 4, 5, 6]
for data in datas:
   if data == 2:
      continue
# Perintah continue diatas, akan menampilkan semua value dalam data
# Tetapi tidak akan menampilkan angka 2, karena angka 2 sedang digunakan untuk pengecekan pengulangan
# dan tidak ada perintah selanjutnya, malah ada continue, jadi perintah pengulangan berhenti
   print(data)
   
print('\n')

bilangans = [1, 2, 3, 4]
for bilangan in bilangans:
   if bilangan == 2 :
      break
# Tapi jika perintahnya adalah break seperti diatas
# Maka, pengulangan akan benar benar berhenti, dan akan menampilkan data bilangan sebelum perintah berhent akibat break
# Hasil dari perintah print dibawah adalah akan tampil bilangan 1
   print(bilangan)