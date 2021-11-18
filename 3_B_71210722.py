#input
bil1 = float(input("Masukan bilangan pertama: "))
bil2 = float(input("Masukan bilangan kedua: "))
kalimat = input("Masukan kalimat: ")

if "kali" in kalimat:
    print("Hasil perkalian", bil1, "dengan", bil2, "adalah", bil1*bil2)
elif "kurang" in kalimat:
    print("Hasil pengurangan", bil1, "dengan", bil2, "adalah", bil1-bil2)
elif "bagi" in kalimat:
    print("Hasil pembagian", bil1, "dengan", bil2, "adalah", bil1/bil2)
elif "tambah" in kalimat:
    print("Hasil penjumlahan", bil1, "dengan", bil2, "adalah", bil1+bil2)
else :
    print("Operator yang anda masukan salah atau tidak ada")
