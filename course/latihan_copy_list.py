# * Teknik menduplikasi list

a = ["Putra", "Rama", "Pratama", "Rangga"]
print(f"data a = {a}")

b = a
print(f"data b = {b}")

a[1] = "botWolf"
b.sort()
# setelah merubah data seperti diatas, tidak hanya a yang berubah, data dalam b juga
# jadi walaupun kita merubah data di salah satu, a atau b, tetap keduanya yang berubah
print(f"data a = {a}")
print(f"data b = {b}")

print(f"address dari a = {hex(id(a))}")
print(f"address dari b = {hex(id(b))}")
# adress dari kedua data diatas adalah sama
# dan akan berubah address memory nya setiap di save
# dan inilah alasan kenapa bila kita rubah data a, data b juga ikut berubah
# dan begitu juga sebaliknya
