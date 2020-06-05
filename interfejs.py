from tkinter import *
from tkinter import messagebox
from tkinter.font import Font


root = Tk()  # okno
root.title("Audiometr")
root.geometry("900x500")
root.config(bg="LightSteelBlue2")
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
start_png = PhotoImage(file="START2.png")
button_start = Button(root, image=start_png, bg='grey95', border='0',
                      command=starting).place(x=50, y=70)

slysze_png = PhotoImage(file="SŁYSZĘ2.png")
button_slysze = Button(root, font=font1, image=slysze_png, bg='grey95', border='0',
                       command=hearing).place(x=45, y=215)

stop_png = PhotoImage(file="STOP2.png")
button_stop = Button(root, font=font1, image=stop_png, bg='grey95', border='0',
                     command=ending).place(x=60, y=360)


#prawa ramka - tu ma być wykres
right_frame = Frame(root, width=600, height=490, bg='grey95')
right_frame.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()
