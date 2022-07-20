from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


mytext1 = ['Morrer afogado',
           'Sempre ficar preso no transito',
           'Ser incapaz de experimentar tristeza',
           'Prevenir a segunda guerra mundial',
           'Ser um mago',
           'Ter o seu maior sonho e pesadelo concretizados']

mytext2 = ['Morrer Queimado',
           'Sempre ter uma internet péssima',
           'Ser incapaz de experimentar de experimentar raiva',
           'Ganhar na loteria', 'Ser um vampiro',
           'Nunca ter nenhum dos seus sonhos concretizados']
i = 0

def escolha():
    global mytext1, mytext2, i
    i += 1
    if i < len(mytext1) and i < len(mytext2):
        n1 = str(b["text"])
        b["text"] = f'1. {mytext1[i]}'
        n2 = str(c["text"])
        c["text"] = f'2. {mytext2[i]}'
    else:
        i = -1

def voltar():
    rot.destroy()
    import inicial

rot = Tk()
rot.title("Trabalho AV2")
rot.geometry('950x500')
rot['bg'] = '#FFE4E1'
rot.wm_iconbitmap('b.ico')  # para inserir um icone ao lado do titulo

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo #avoid garbage collection

#Redimencionar a imagem
image = Image.open('pink.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(rot, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

a = Label(rot,
          text='Você prefere:',
          fg='black',
          font='oswald 30 bold',
          bg='#FFC0CB',
          bd='2px'
          )

a.place(x=350, y=0)

b = Label(rot,
          text=f'1. {mytext1[0]}',
          fg='black',
          font='oswald 20 bold',
          bg='#B0E0E6',
          bd='2px'
          )
b.place(x=210, y=100)

c = Label(rot,
          text=f'2. {mytext2[0]}',
          fg='black',
          font='oswald 20 bold',
          bg='#EEE8AA',
          bd='2px'
          )
c.place(x=210, y=200)

op1 = Button(rot, text='1', bg='#B0E0E6', bd='2px', font='oswald 40 bold', command=escolha)
op1.place(x=250, y=300)

op2 = Button(rot, text='2', bg='#EEE8AA', bd='2px', font='oswald 40 bold', command=escolha)
op2.place(x=500, y=300)

op3 = Button(rot, text='Sair', bg='red', bd='2px', font='oswald 15 bold', command=rot.destroy)
op3.place(x=790, y=380)

op4 = Button(rot, text='Inicio', bg='pink', bd='2px', font='oswald 15 bold', command=voltar)
op4.place(x=700, y=380)

rot.mainloop()
