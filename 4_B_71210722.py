#input
bil = int(input("Masukan angka: "))

if ((bil %2 == 0) and (bil %3 ==1)):
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: YA \n")
    if ((bil %5 ==1) or (bil %10 == 0)):
        print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
    else :
        print("Apakah Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")
else :
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")
