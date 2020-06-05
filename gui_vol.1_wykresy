from tkinter import *
from tkinter import messagebox
import audiometr as play
import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

root = Tk() #okno
root.title("Audiometr")
root.geometry("900x500")
root.config(bg="skyblue")
#----------------------------------------------------------------------------------
oktawa = play.odtwarzanie() #oktawa odtwarza i zatrzymuje dany plik,zmienną
lista_plikow = ["125L.wav", "250L.wav", "500L.wav", "1kL.wav", "2kL.wav", "4kL.wav", "8kL.wav", "125P.wav", "250P.wav", "500P.wav", "1kP.wav", "2kP.wav", "4kP.wav", "8kP.wav"]
czestotliwosci = ["125", "250", "500", "1000", "2000", "4000", "8000"]
czasy_slyszalnosci_lewe = []
czasy_slyszalnosci_prawe = []
#---------------------------------------------------------------------------------
def starting():
    global start, i
    i =0
    print("Próba dla lewego ucha.")
    start = time.time()
    oktawa.odtwarzanie(lista_plikow[i])


def hearing():
    global i, start
    if i < len(lista_plikow)-1:
        koniec = time.time()
        oktawa.stop()
        czas = koniec - start
        if i < 7:
            czasy_slyszalnosci_lewe.append(czas)
        if i >= 7:
            czasy_slyszalnosci_prawe.append(czas)
        if i == 6:
            print("Teraz prawe ucho.")
        i = i + 1
        start = time.time()
        oktawa.odtwarzanie((lista_plikow[i]))
    else:
        koniec = time.time()
        oktawa.stop()
        czas = koniec - start
        czasy_slyszalnosci_prawe.append(czas)
        #wykres z wynikami
        f, a = plt.subplots()
        a.plot(czestotliwosci, czasy_slyszalnosci_lewe, label= "Lewe ucho", marker= "o", markersize= 10)
        a.plot(czestotliwosci, czasy_slyszalnosci_prawe, label= "Prawe ucho", marker= "x", markersize= 10)
        plt.title("Wyniki badania", size= 20)
        plt.xlabel("Częstotliwość (Hz)")
        plt.ylabel("Czas usłyszenia (sekundy)")
        a.grid()
        plt.legend()
        canvas = FigureCanvasTkAgg(f, root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=5)

def ending():
    root.destroy()

#lewa ramka
left_frame = Frame(root, width=200, height=490, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

#przyciski
button_start = Button(root, text="start", padx=75, pady=50,command = starting).place(x=20, y=20)
button1 = Button(root, text="słyszę", padx=71, pady=50,command = hearing).place(x=20, y=170)
button_stop = Button(root, text="stop", padx=72, pady=50, command = ending).place(x=20, y=320)


#prawa ramka - tu ma być wykres

right_frame = Frame(root, width=650, height=490, bg='grey')

root.mainloop()
