from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import font

root = Tk()  # okno
root.title("Audiometr")
root.geometry("900x500")
root.config(bg="LightSteelBlue1")
font1 = Font(family='Verdana', size=10)
fonts = list(font.families())
print(fonts)

#puste funkcje
def starting():
    messagebox.showinfo("Audiometr", "Start")


def hearing():
    messagebox.showinfo("Audiometr", "Usłyszano")


def ending():
    messagebox.showinfo("Audiometr", "End")

#lewa ramka
left_frame = Frame(root, width=200, height=490, bg='grey')
left_frame.grid(row=0, column=0, padx=10, pady=5)

#przyciski
start_png = PhotoImage(file="START.png")
# button_start = Button(root, font=font1, text="START", padx=68, pady=50, command=starting).place(x=20, y=20)
button_start = Button(root, image=start_png, bg='grey', border='0', command=starting).place(x=20, y=20)

button1 = Button(root, font=font1, text="SŁYSZĘ", padx=65, pady=50, command=hearing).place(x=20, y=170)

button_stop = Button(root, font=font1, text="STOP", padx=71, pady=50, command=ending).place(x=20, y=320)
#prawa ramka - tu ma być wykres
right_frame = Frame(root, width=650, height=490, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()