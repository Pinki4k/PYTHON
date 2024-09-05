import os
import datetime
from tkinter import Tk, messagebox

def abrirCalculadora():
    os.system("calc")

def mostrarhora():
    hora = datetime.datetime.now()
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo(message=f"{hora.year}", title="La hora")
    root.destroy()  # Destruye la ventana después de mostrar el mensaje

abrirCalculadora()
mostrarhora()