import tkinter as tk

from tkinter import *
from PIL import Image
from pynput.mouse import Button, Controller, Listener

cw = 600
ch = 600

root = Tk()
root.title("Electric field visualizer")
root.maxsize(cw, ch)
mouse = Controller()

# adicionar um canvas na tela
canvas = Canvas(root, height=ch, width=cw, bg="black")
canvas.grid(column=0, row=2)

# armazenar as cargas em um vetor
pos = []
neg = []
grid = []


# desenhar grade
def draw_grid():
    if size.get() > 0:
        scl = int(cw / size.get())

        canvas.delete("all") # deletar todos os elementos do canvas ao inserir um novo tamanho de grade

        # deletar os elementos do vetor ao resetar o canvas
        del pos[:]
        del neg[:]
        del grid[:]

        i = 0
        while i < cw:
            canvas.create_line(0, i, cw, i, fill="gray", width=1)  # linhas horizontais
            canvas.create_line(i, 0, i, ch, fill="gray", width=1)  # linhas verticais
            i += scl



# determinar o tamanho da grade do canvas
size = tk.IntVar()
size_box = tk.Entry(root, width=30, textvariable=size)
size_box.grid(column=0, row=0)

# botão para enviar o tamanho da grade
submit = tk.Button(root, text="Enviar", width=10, command=draw_grid)
submit.grid(column=0, row=1)


# desenhar os vetores
def draw_vector():
    for i in range(int(ch / 60)):
        for j in range(int(cw / 60)):
            canvas.create_line(j * 60 + 10, i * 60 + 10, j * 60 + 50, i * 60 + 50, fill="white", arrow="last", width=3)


def create_grid_arr(scl):
    # iniciar a matriz grade do canvas
    grid = [None] * int(cw / scl)
    for i in range(int(cw / scl)):
        grid[i] = [None] * int(cw / scl)

    return grid


# adicionar as cargas na tela
def insert_pos(event):
    x, y = event.x, event.y

    if size.get() > 0:
        _scl = int(cw / size.get())

    global grid
    if len(grid) == 0:
        grid = create_grid_arr(_scl)

    # redimensionar o tamanho da imagem em relação a escala da grade
    img = Image.open("Positive.png")
    img = img.resize((_scl,_scl), Image.ANTIALIAS)
    img.save('resized_pos.png')
    pos.append(PhotoImage(file="resized_pos.png"))

    # ajustar a posição do mouse em relação a grade
    i = int(y / _scl)
    j = int(x / _scl)
    x = _scl * j + img.size[0]/2
    y = _scl * i  + img.size[1]/2

    # colocar a imagem no canvas
    canvas.create_image(x, y, image=pos[len(pos) - 1])
    canvas.image = pos[len(pos) - 1]

    # inserir carga na matriz da grade
    grid[i][j] = pos[len(pos) - 1]


def insert_neg(event):
    x, y = event.x, event.y

    if size.get() > 0:
        _scl = int(cw / size.get())

    global grid
    if len(grid) == 0:
        grid = create_grid_arr(_scl)

    img = Image.open("Negative.png")
    img = img.resize((_scl, _scl), Image.ANTIALIAS)
    img.save('resized_neg.png')
    neg.append(PhotoImage(file="resized_neg.png"))

    i = int(y / _scl)
    j = int(x / _scl)
    x = _scl * j + img.size[0]/2
    y = _scl * i + img.size[1]/2

    canvas.create_image(x, y, image=neg[len(neg) - 1])
    canvas.image = neg[len(neg) - 1]

    grid[i][j] = pos[len(pos) - 1]


# funções para o mouse
canvas.bind('<Button-1>', insert_pos)
canvas.bind('<Button-3>', insert_neg)


#funcoes do console
def add_particle():
    print(console.get())


# console
console_title= Label(root,text="Console",bg="black",fg="white")
console_title.place(x=10,y=550)
console = tk.StringVar()
console_box = tk.Entry(root,justify=LEFT,width=40 ,bg="gray",fg="white",bd=0,textvariable=console)
console_box.place(x=10,y=570)
console_button = tk.Button(root,text="Enviar",width=5,bd=0,command=add_particle)
console_button.place(x=350, y=570)

mainloop()
