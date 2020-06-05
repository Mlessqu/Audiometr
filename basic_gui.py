from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from PIL import Image, ImageTk
import audiometr as play
import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


root = Tk()
root.title("Audiometr")
root.iconbitmap("wave.ico")
root.geometry("900x500")
root.config(bg="LightSteelBlue2")
font1 = Font(family='Verdana', size=10)
#----------------------------------------------------------------------------------
oktawa = play.odtwarzanie() #oktawa odtwarza i zatrzymuje dany plik,zmienną
lista_plikow = ["125L.wav", "250L.wav", "500L.wav", "1kL.wav", "2kL.wav", "4kL.wav", "8kL.wav", "125P.wav", "250P.wav", "500P.wav", "1kP.wav", "2kP.wav", "4kP.wav", "8kP.wav"]
czestotliwosci = ["125", "250", "500", "1000", "2000", "4000", "8000"]
czasy_slyszalnosci_lewe = []
czasy_slyszalnosci_prawe = []
#---------------------------------------------------------------------------------

def rozpocznij():
    root.destroy()
    root2 = Tk()  # okno
    root2.iconbitmap("wave.ico")
    root2.title("Audiometr")
    root2.geometry("900x500")
    root2.config(bg="LightSteelBlue2")

    # puste funkcje
    def starting():
        global start, i
        i = 0
        print("Próba dla lewego ucha.")
        start = time.time()
        oktawa.odtwarzanie(lista_plikow[i])
        button_start = Button(root2, image=start_png, bg='grey95', border='0', state='disabled',
                              command=starting).place(x=50, y=70)

    def hearing():
        global i, start
        if i < len(lista_plikow) - 1:
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
            # wykres z wynikami
            f, a = plt.subplots()
            a.plot(czestotliwosci, czasy_slyszalnosci_lewe, label="Lewe ucho", marker="o", markersize=10)
            a.plot(czestotliwosci, czasy_slyszalnosci_prawe, label="Prawe ucho", marker="x", markersize=10)
            plt.title("Wyniki badania", size=20)
            plt.xlabel("Częstotliwość (Hz)")
            plt.ylabel("Czas usłyszenia (sekundy)")
            a.grid()
            plt.legend()
            canvas = FigureCanvasTkAgg(f, root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=5)

    def ending():
        try:
            root2.destroy()
        except:
            pass

    # lewa ramka
    left_frame = Frame(root2, width=250, height=490, bg='grey95')
    left_frame.grid(row=0, column=0, padx=10, pady=5)

    # przyciski
    start_png = tk.PhotoImage(file="START2.png")
    button_start = Button(root2, image=start_png, bg='grey95', border='0',
                          command=starting).place(x=50, y=70)

    slysze_png = tk.PhotoImage(file="SŁYSZĘ2.png")
    button_slysze = Button(root2, font=font1, image=slysze_png, bg='grey95', border='0',
                           command=hearing).place(x=45, y=215)

    stop_png = tk.PhotoImage(file="STOP2.png")
    button_stop = Button(root2, font=font1, image=stop_png, bg='grey95', border='0',
                         command=ending).place(x=60, y=360)

    instrukcja_png = Image.open("instrukcja.PNG")
    instrukcjaTk = ImageTk.PhotoImage(instrukcja_png)
    lab = Label(image=instrukcjaTk).place(x=300, y=105)

    #
    # # prawa ramka - tu ma być wykres
    # right_frame = Frame(root2, width=600, height=490, bg='grey95')
    # right_frame.grid(row=0, column=1, padx=10, pady=5)

    root2.mainloop()


label = tk.Label(text="Audiometr", bg="LightSteelBlue2", fg='grey26', font=('Verdana', 32, 'bold')).place(x=305, y=130)

rozpocznij_png = PhotoImage(file="ROZPOCZĘCIE.png")
przycisk_rozpocznij = Button(root, image=rozpocznij_png, bg="LightSteelBlue2", border='0',
                             command=rozpocznij).place(x=280, y=300)

# jeśli zdecydujemy się np. pokazywać wyniki badania to można dodać tą opcje do menu
# pasekMenu = Menu(root)
# pomocMenu = Menu(pasekMenu, tearoff=0)
# pomocMenu.add_command(label="Wyjdź", command=root.quit)
# pasekMenu.add_cascade(label="Opcje", menu=pomocMenu)
#
# root.config(menu=pasekMenu)
root.mainloop()