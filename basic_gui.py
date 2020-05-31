from tkinter import *
from tkinter import messagebox

root = Tk() #okno
root.title("Audiometr")
root.geometry("900x500")
root.config(bg="skyblue")

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
button_start = Button(root, text="start", padx=75, pady=50,command = starting ).place(x=20, y=20)
button1 = Button(root, text="słyszę", padx=71, pady=50,command = hearing ).place(x=20, y=170)
button_stop = Button(root, text="stop ", padx=72, pady=50, command = ending ).place(x=20, y=320)
#prawa ramka - tu ma być wykres
right_frame = Frame(root, width=650, height=490, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)




root.mainloop()
