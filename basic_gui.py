import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import audiometr as play
import time
import matplotlib.pyplot as plt
root = Tk() #okno
root.title("Audiometr")
root.geometry("900x500")
root.config(bg="skyblue")
#----------------------------------------------------------------------------------
oktawa = play.odtwarzanie() #oktawa odtwarza i zatrzymuje dany plik,zmienną
lista_plikow = ["125.wav", "250.wav", "500.wav", "1k.wav", "2k.wav", "4k.wav", "8k.wav"]
czestotliwosci = ["125", "250", "500", "1000", "2000", "4000", "8000"]
lista_decybeli = []
czasy_slyszalnosci = []
#---------------------------------------------------------------------------------
def starting():
    global start, i
    i =0
    start = time.time()
    oktawa.odtwarzanie(lista_plikow[i])


def hearing():
    global i, start
    if i < len(lista_plikow)-1:
        koniec = time.time()
        oktawa.stop()
        czas = koniec - start
        czasy_slyszalnosci.append(czas)
        i = i + 1
        start = time.time()
        oktawa.odtwarzanie((lista_plikow[i]))
    else:
        koniec = time.time()
        oktawa.stop()
        czas = koniec - start
        czasy_slyszalnosci.append(czas)

        plt.plot(czestotliwosci, czasy_slyszalnosci, label="wszystkie uszy dopóki nie ogarniamy", marker="x",
                     markersize=10)
        plt.title("Wyniki badania")
        plt.xlabel("Częstotliwość (Hz)")
        plt.ylabel("Glośność (dB)")
        plt.legend()
        plt.grid()


def results(msg):
    popup = tk.Tk()
    popup.wm_title("Koniec badania")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Wyniki", command=plt.show())
    B1.pack()
    popup.mainloop()

def ending():
    root.destroy()

#lewa ramka
left_frame = Frame(root, width=200, height=490, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

#przyciski
button_start = Button(root, text="start", padx=75, pady=50,command = starting ).place(x=20, y=20)
button1 = Button(root, text="słyszę", padx=71, pady=50,command = hearing ).place(x=20, y=170)
button_stop = Button(root, text="stop ", padx=72, pady=50, command = ending ).place(x=20, y=320)

#prawa ramka - tu ma być wykres
right_frame = Frame(root, width=650, height=490, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)




root.mainloop()
