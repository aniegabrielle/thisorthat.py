from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox


def voltar():
    root.destroy()
    import inicial


def acesso():
    nickname = E_nick.get()
    pw = E_senha.get()
    try:
        con = mysql.connect(host='localhost', user='root', password='', database='trabalhoAV2')
        cursor = con.cursor()
        cursor.execute(
            "select * from jogador where nick = ' " + nickname + " ' and senha = ' " + pw + " ' ")
        dados = cursor.fetchall()
        if dados != ' ' and nickname in dados[0][0]:
            MessageBox.showinfo(title='Aviso', message='Logado com sucesso!')
            root.destroy()
            import perguntas
    except:
        MessageBox.showinfo(title='Aviso',
                            message='Erro ao fazer login, usuário e/ou senha incorretos ou inexistentes.')


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo  # avoid garbage collection


root = Tk()
root.title("Trabalho AV2")
root.geometry('950x500')
root['bg'] = '#FFE4E1'
root.wm_iconbitmap('b.ico')  # para inserir um icone ao lado do titulo

# Redimencionar a imagem
image = Image.open('n.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand=YES)

a = Label(root,
          text='Por favor,\npreencha os dados abaixo:',
          fg='black',
          font='oswald 20 bold',
          bg='lightblue',
          bd='2px'
          )

a.place(x=290, y=60)

nick = Label(root, text='Nick:  ', font='oswald 15 bold',
             bg='lightblue')
nick.place(x=380, y=180)

senha = Label(root, text='Senha:  ', font='oswald 15 bold',
              bg='lightblue')
senha.place(x=360, y=240)

# BOX
E_nick = Entry()
E_nick.place(x=470, y=185)

E_senha = Entry(show='*')
E_senha.place(x=470, y=245)

l1 = Button(root, text='Cancelar', bg='#B0E0E6', bd='2px', font='oswald 15 bold', command=voltar)
l1.place(x=340, y=320)

l2 = Button(root, text='Login', bg='#EEE8AA', bd='2px', font='oswald 15 bold', command=lambda: acesso())
l2.place(x=540, y=320)

l4 = Button(root, text='Sair', bg='red', bd='2px', font='oswald 15 bold', command=root.destroy)
l4.place(x=750, y=380)

root.mainloop()
