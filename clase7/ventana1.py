from tkinter import *
from tkinter import ttk, messagebox
from controladores import abrirCalculadora, mostrarhora

ventana = Tk()
ventana.title("Primera Ventana")
ventana.geometry("520X420")
#ventana.iconbitmap("logo.ico")
botonCalculadora = Button(text ="Calculadora", command=abrirCalculadora)
botonCalculadora.place(x=50, y=50)
botonHora = Button(text="la hora", command=mostrarhora)
botonHora.place(x=150, y=50)

ventana.mainloop()