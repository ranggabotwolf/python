# Control Statement
condition = False

if condition == True:
    print("The Condition")
    print("was True")
else:
    print("The Condition")
    print("was False")

print("\n")
# Contoh lain
condition = True
name = "Rangga"

if condition == True:
    print("The Condition")
    print("was True")
elif name == "Rangga":
    print("Hi, Rangga")
elif name == "Putra":
    print("Hi, Putra")
elif name == "Pratama":
    print("Hi, Pratama")
else:
    print("The condition")
    print("was False")
# Perintah diatas akan berhenti pada if yang pertama, kenapa? karena if yang pertama bernilai benar, dan program akan berhenti samapi disitu

print("\n")
# Sementara itu, perintah dibawah akan berlanjut, karena if condition yang pertama sudah salah, maka program akan berlanjut ke elif selanjutnya samapi menemukan yang benar
condition = False
name = "Rangga"

if condition == True:
    print("The Condition")
    print("was True")
elif name == "Rangga":
    print("Hi, Rangga")
elif name == "Putra":
    print("Hi, Putra")
elif name == "Pratama":
    print("Hi, Pratama")
else:
    print("The condition")
    print("was False")
