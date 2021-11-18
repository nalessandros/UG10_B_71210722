#input
huruf = input("Masukan nilai huruf PrakTekkom anda: ")

print("========================")

if huruf == "A":
    print("Rentang nilai PrakTekkom anda adalah 85 - 100")
elif huruf == "A-":
    print("Rentang nilai PrakTekkom anda adalah 80 - 84")
elif huruf == "B+":
    print("Rentang nilai PrakTekkom anda adalah 75 - 79")
elif huruf == "B":
    print("Rentang nilai PrakTekkom anda adalah 70 - 74")
elif huruf == "B-":
    print("Rentang nilai PrakTekkom anda adalah 65 - 69")
elif huruf == "C+":
    print("Rentang nilai PrakTekkom anda adalah 60 - 64")
elif huruf == "C":
    print("Rentang nilai PrakTekkom anda adalah 55 - 59")
elif huruf == "D":
    print("Rentang nilai PrakTekkom anda adalah 45 - 54")
elif huruf == "E":
    print("Rentang nilai PrakTekkom anda adalah 0 - 44")
else :
    print("Inputan anda salah atau nilai huruf tidak ada pada Standar Nilai")

