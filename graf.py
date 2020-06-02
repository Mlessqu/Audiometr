import matplotlib.pyplot as plt

fr = ["125", "250", "500", "1000", "2000", "4000", "8000"]
left_ear = [1, 2, 3, 4, 5, 6, 7] ##### tu potrzebuję wyników
right_ear = [2, 5, 8, 6, 9, 9, 8] ##### pewnie w innej formie

plt.plot(fr, left_ear, label= "Lewe ucho", marker= "o", markersize= 10)
plt.plot(fr, right_ear, label="Prawe ucho", marker= "x", markersize= 10)


plt.title("Audiogram")
plt.xlabel("Częstotliwość (Hz)")
plt.ylabel("Glośność (dB)")
plt.legend()
plt.show()