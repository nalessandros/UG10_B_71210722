#input
rsi = int(input("Masukan besar RSI: "))
macd = input("Masukan kondisi MACD: ")

if (rsi >= 70) and (macd == "death-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")
elif (rsi <= 30) and (macd == "golden-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya Beli")
elif (rsi >= 70) and (macd == "golden-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")
elif (rsi <= 30) and (macd == "death-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai Golden-cross")
else :
    print("RSI berada di area 30 - 70, Bukan saatnya membeli maupun menjual")
