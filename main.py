import _tkinter as tk

from tkinter import *
from PIL import Image
from pynput.mouse import Button, Controller, Listener

root = Tk()
mouse = Controller()

cw = 600
ch = 600

# adicionar um canvas na tela
canvas = Canvas(root, height=ch, width=cw, bg="black")
canvas.pack()

# armazenar as cargas em um vetor
pos=[]
neg=[]

# desenhar os vetores
def draw_vector():
    for i in range(int(ch / 60)):
        for j in range(int(cw / 60)):
            canvas.create_line(j*60, i*60, j*60 + 40, i*60 + 40, fill="white", arrow="last", width=3)

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

draw_vector()

mainloop()