# Program konversi temperatur

print("PROGRAM KONVERSI TEMPERATUR\n")

print("*" * 30)
celcius = float(input("Masukkan suhu dalam celcius :"))
print("Suhu dalam celsius :", celcius, "celcius")

reamur = (4 / 5) * celcius
fahrenheit = ((9 / 5) * celcius) + 32
kelvin = celcius + 273
print("Suhu dalam Reamur :", reamur, "Reamur")
print("Suhu dalam Fahrenheit :", fahrenheit, "Fahrenheit")
print("Suhu dalam Kelvin :", kelvin, "Kelvin")
print("\n")

print("*" * 30)
reamur = float(input("Masukkan suhu dalam reamur :"))
print("Suhu dalam reamur :", reamur, "reamur")

celcius = (5 / 4) * reamur
fahrenheit = ((9 / 4) * reamur) + 32
kelvin = ((5 / 4) * reamur) + 273
print("Suhu dalam celcius :", celcius, "celcius")
print("Suhu dalam Fahrenheit :", fahrenheit, "Fahrenheit")
print("Suhu dalam Kelvin :", kelvin, "Kelvin")
print("\n")

print("*" * 30)
fahrenheit = float(input("Masukkan suhu dalam fahrenheit :"))
print("Suhu dalam fahrenheit :", fahrenheit, "fahrenheit")

celcius = (5 / 9) * (fahrenheit - 32)
reamur = (4 / 9) * (fahrenheit - 32)
kelvin = celcius + 273
print("Suhu dalam celcius :", celcius, "celcius")
print("Suhu dalam reamur :", reamur, "reamur")
print("Suhu dalam Kelvin :", kelvin, "Kelvin")
print("\n")

print("*" * 30)
kelvin = float(input("Masukkan suhu dalam kelvin :"))
print("Suhu dalam kelvin :", kelvin, "kelvin")

celcius = kelvin - 273
reamur = (4 / 5) * (kelvin - 273)
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu dalam celcius :", celcius, "celcius")
print("Suhu dalam reamur :", reamur, "reamur")
print("Suhu dalam Fahrenheit :", fahrenheit, "Fahrenheit")
print("\n")
