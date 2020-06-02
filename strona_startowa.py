from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

root = Tk()
root.title("Audiometr")
root.iconbitmap(r"C:\Users\annak\Desktop\python\Audiometr\Audiometr\wave.ico")
root.geometry("900x500")
root.config(bg="LightSteelBlue2")
font1 = Font(family='Verdana', size=10)


def rozpocznij():
    root.destroy()
    root2 = Tk()  # okno
    root2.iconbitmap(r"C:\Users\annak\Desktop\python\Audiometr\Audiometr\wave.ico")
    root2.title("Audiometr")
    root2.geometry("900x500")
    root2.config(bg="LightSteelBlue2")

    # puste funkcje
    def starting():
        messagebox.showinfo("Audiometr", "Start")

    def hearing():
        messagebox.showinfo("Audiometr", "Usłyszano")

    def ending():
        messagebox.showinfo("Audiometr", "End")

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

    # prawa ramka - tu ma być wykres
    right_frame = Frame(root2, width=600, height=490, bg='grey95')
    right_frame.grid(row=0, column=1, padx=10, pady=5)

    root2.mainloop()


label = tk.Label(text="Audiometr", bg="LightSteelBlue2", fg='grey26', font=('Verdana', 32, 'bold')).place(x=305, y=130)

rozpocznij_png = PhotoImage(file="ROZPOCZĘCIE.png")
przycisk_rozpocznij = Button(root, image=rozpocznij_png, bg="LightSteelBlue2", border='0',
                             command=rozpocznij).place(x=280, y=300)

#jeśli zdecydujemy się np. pokazywać wyniki badania to można dodać tą opcje do menu
# pasekMenu = Menu(root)
# pomocMenu = Menu(pasekMenu, tearoff=0)
# pomocMenu.add_command(label="Wyjdź", command=root.quit)
# pasekMenu.add_cascade(label="Opcje", menu=pomocMenu)
#
# root.config(menu=pasekMenu)
root.mainloop()
