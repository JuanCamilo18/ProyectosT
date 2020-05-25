# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import colorchooser

ventana  = Tk()
ventana.title("Dibujo en Turtle V1.0")
ventana.configure(bd = 10)

lona = Canvas(ventana, width=601, height=511, bg="Gainsboro")
lona.grid(column=0, row=0, columnspan=2)

def color1(event):
    current = event.widget.find_withtag('current')
    item = current[0]
    lona.itemconfigure(item, fill = color, outline = color)

def color2(event):
    current = event.widget.find_withtag('current')
    item = current[0]
    lona.itemconfigure(item, fill = "Ghost White", outline = "Gainsboro")

def nuevo():
    cuadricula()


color = "Blue Violet"

def paleta():
    global color
    c = colorchooser.askcolor()
    color = c[1]
    boton1.configure(bg = color)

def guardar():
    lona.postscript(file = "Pixel_ima.eps")


boton1 = Button(ventana, height=2, bg=color, bd=0, cursor="hand2", command=paleta)
boton1.grid(column=0, row=1, columnspan=2, pady=2, sticky=E+W)
boton2 = Button(ventana, text="Guardar", height=2, cursor="hand2", command=guardar)
boton2.grid(column=0, row=2, sticky=E+W)
boton3 = Button(ventana, text="Nuevo", height=2, cursor="hand2", command=nuevo)
boton3.grid(column=1, row=2, sticky=E+W)


def cuadricula():
    for y in range(2, 500, 15):
        for x in range(2, 600, 15):
            cua = lona.create_rectangle(x,y, x+15, y+15, fill='Ghost White', width=1, outline='Gainsboro')
            lona.tag_bind(cua, '<Button-1>', color1)
            lona.tag_bind(cua, '<Button-3>', color2)


cuadricula()    

ventana.mainloop()



