import tkinter as tk

from tkinter import *
from PIL import Image
from pynput.mouse import Button, Controller, Listener

cw = 600
ch = 600

root =Tk()
root.title("Electric field visualizer")
root.maxsize(cw, ch)
mouse = Controller()

# adicionar um canvas na tela
canvas = Canvas(root, height=ch, width=cw, bg="black")
canvas.grid(column=0, row=0)

# armazenar as cargas em um vetor
pos=[]
neg=[]


# desenhar grid
def draw_grid():
    scl = int(cw/size.get())

    i = 0
    canvas.delete("all")
    while i < cw:
        canvas.create_line(0, i, cw, i, fill="gray", width=1)  # linhas horizontais
        canvas.create_line(i, 0, i, ch, fill="gray", width=1)  # linhas verticais
        i += scl


# determinar o tamanho da grade do canvas
size = tk.IntVar()
size_box = tk.Entry(root, width=30, textvariable=size)
size_box.place(x=10, y=10)

submit = tk.Button(root, text="Enviar", width=10, command=draw_grid)
submit.place(x=10, y=40)


# adicionar as cargas na tela
def insert_pos(event):
    x, y = event.x, event.y

    pos.append(PhotoImage(file="resized_pos.png"))

    for img in pos:
        canvas.create_image(x, y, image=img)
        canvas.image = img


def insert_neg(event):
    x, y = event.x, event.y

    neg.append(PhotoImage(file="resized_neg.png"))

    for img in neg:
        canvas.create_image(x, y, image=img)
        canvas.image = img


# funções para o mouse
root.bind('<Button-1>', insert_pos)
root.bind('<Button-3>', insert_neg)

mainloop()
