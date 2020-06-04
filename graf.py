import matplotlib.pyplot as plt

fr = ["125", "250", "500", "1000", "2000", "4000", "8000"]
left_ear = [1, 2, 3, 4, 5, 6, 7] ##### tu potrzebuję wyników
right_ear = [2, 5, 8, 6, 9, 9, 8] ##### pewnie w innej formie

# plt.plot(fr, left_ear, label= "Lewe ucho", marker= "o", markersize= 10)
plt.plot(fr, , label="wszystkie uszy dopóki nie ogarniamy", marker= "x", markersize= 10)


plt.title("Audiogram")
plt.xlabel("Częstotliwość (Hz)")
plt.ylabel("Glośność (dB)")
plt.legend()
plt.grid()
plt.show()

for j in range(len(czasy_slyszalnosci)):
    print("Plik:" + lista_plikow[j])
    print("Usłyszano po:" + str(czasy_slyszalnosci[j]))
    dB = czasy_slyszalnosci[j] * 1 / 30 * 2  # 1/30 bo 30s trwa zmiana z 0 do 1 amplitudy(sciezka audio)
    # a jedna zmiana amplitudy się przekłada(chyba, badz w tym przypadku) na 2dB
    db = dB - 60  # maksymalna wartość to 0 więc odejmuję 60
    print("Decybele w tym momencie to:" + str(dB))