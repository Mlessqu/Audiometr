from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import font

root = Tk()  # okno
root.title("Audiometr")
root.geometry("900x500")
root.config(bg="LightSteelBlue1")
font1 = Font(family='Verdana', size=10)

#puste funkcje
def starting():
    messagebox.showinfo("Audiometr", "Start")


def hearing():
    messagebox.showinfo("Audiometr", "Usłyszano")


def ending():
    messagebox.showinfo("Audiometr", "End")

#lewa ramka
left_frame = Frame(root, width=250, height=490, bg='grey95')
left_frame.grid(row=0, column=0, padx=10, pady=5)

#przyciski
start_png = PhotoImage(file="START.png")
button_start = Button(root, image=start_png, bg='grey95', border='0',
                      command=starting).place(x=40, y=50)

slysze_png = PhotoImage(file="SŁYSZĘ.png")
button_slyszę = Button(root, font=font1, image=slysze_png, bg='grey95', border='0',
                       command=hearing).place(x=30, y=200)

stop_png = PhotoImage(file="STOP.png")
button_stop = Button(root, font=font1, image=stop_png, bg='grey95', border='0',
                     command=ending).place(x=50, y=350)

#prawa ramka - tu ma być wykres
right_frame = Frame(root, width=600, height=490, bg='grey95')
right_frame.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()