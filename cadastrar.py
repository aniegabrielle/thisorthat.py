from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

#cursor.execute('create database trabalhoAV2')

raiz = Tk()
raiz.title("Trabalho AV2")
raiz.geometry('1000x500')
raiz['bg'] = '#FFE4E1'
raiz.wm_iconbitmap('b.ico')  # para inserir um icone ao lado do titulo


def inserir():
    nick = e_nick.get()
    nome = e_nome.get()
    senha = e_senha.get()
    email = e_email.get()
    try:
        if(nick =='' or nome =='' or senha =='' or email ==''):
            MessageBox.showinfo('Status inserido', 'Todos os campos são obrigatórios.')
        else:
            con = mysql.connect(host='localhost', user='root', password='', database='trabalhoAV2')
            cursor = con.cursor()
            '''cursor.execute('create table jogador(nick varchar(10) primary key, nome varchar(20) ,\
                                    senha int(10) , email varchar(150))')'''
            cursor.execute("insert into jogador values(' "+nick+" ', ' "+nome+" ', ' "+senha+" ', ' "+email+" ')")
            cursor.execute('commit')
            MessageBox.showinfo('Status inserido','Inserido com sucesso!')
            con.close()
            raiz.destroy()
            import login

    except:
        MessageBox.showinfo(title='Aviso',
                            message='Nick já existe.')



def voltar():
    raiz.destroy()
    import inicial


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo #avoid garbage collection

#Redimencionar a imagem
image = Image.open('n.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(raiz, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

a = Label(raiz,
          text='Por favor, preencha os dados abaixo:',
          fg='black',
          font='oswald 20 bold',
          bg='lightblue',
          bd='2px'
          )

a.place(x=270, y=60)

nick = Label( raiz, text = 'Nick:  ', font='oswald 15 bold',
          bg='lightblue')
nick.place(x = 415, y = 120)

nome = Label( raiz , text = 'Nome:  ', font='oswald 15 bold',
          bg='lightblue')
nome.place(x = 402, y = 165)

senha = Label( raiz , text = 'Senha:  ', font='oswald 15 bold',
          bg='lightblue')
senha.place(x = 399, y = 210)

email = Label( raiz , text = 'E-mail:  ', font='oswald 15 bold',
          bg='lightblue')
email.place(x = 398, y = 255)

#BOX
e_nick = Entry()
e_nick.place(x = 500, y = 125)

e_nome = Entry()
e_nome.place(x = 500 , y = 170)

e_senha = Entry(show = '*')
e_senha.place(x = 500 , y = 215)

e_email = Entry()
e_email.place(x = 500 , y = 260)

c1 = Button(raiz, text='Cancelar', bg='#B0E0E6', bd='2px', font='oswald 15 bold', command=voltar)
c1.place(x=350, y=320)

c2 = Button(raiz, text='Cadastrar', bg='#EEE8AA', bd='2px', font='oswald 15 bold', command=inserir)
c2.place(x=550, y=320)

c3 = Button(raiz, text='Inicio', bg='pink', bd='2px', font='oswald 15 bold', )
c3.place(x=120, y=370)

c4 = Button(raiz, text='Sair', bg='red', bd='2px', font='oswald 15 bold', command=raiz.destroy)
c4.place(x=790, y=380)

raiz.mainloop()