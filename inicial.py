from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Criando as janelas
rt = Tk()
rt.title("Trabalho AV2")
rt.geometry('950x500')
rt['bg'] = '#FFE4E1'
rt.wm_iconbitmap('b.ico')  # para inserir um icone ao lado do titulo


# Funções...

# Janela de login --------------------------------------------------------------------
def login():
    rt.destroy()
    import login
# Final do login ---------------------------------------------------------------------------

# Janela de cadastro --------------------------------------------------------------------
def cadastro():
    rt.destroy()
    import cadastrar
# Final do cadastro ---------------------------------------------------------------------------

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


# Redimencionar a imagem
image = Image.open('IA.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(rt, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

# Label - rotulo
a = Label(rt,
          text='Bem vindo!\n '
               'Escolha uma opção para começar',
          fg='black',
          font='oswald 20 bold',
          bg='#FFC0CB',
          bd='2px'
          )

a.place(x=250, y=0)

# Button - para criar um botão
i1 = Button(rt, text='Cadastrar', bg='#B0E0E6', bd='2px', font='oswald 20 bold', command=cadastro)
i1.place(x=70, y=20)

i2 = Button(rt, text='Login', bg='#EEE8AA', bd='2px', font='oswald 20 bold', command=login)
i2.place(x=750, y=20)

i3 = Button(rt, text='Sair', bg='red', bd='2px', font='oswald 20 bold', command=rt.quit)
i3.place(x=800, y=390)

rt.mainloop()
# termino programa principal
