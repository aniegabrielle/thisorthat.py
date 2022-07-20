from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as MessageBox

conexao = mysql.connect(  # usei o pycharm e com ele não precisa colocar .connector
    host='localhost',
    user='root',
    passwd='',
    database='provaav2'
)

cursor = conexao.cursor()

# cursor.execute('create database provaav2')

'''cursor.execute('create table usuario(login varchar(10) primary key, nome varchar(20) ,\
                                    senha int(10) , email varchar(150))')

sql = 'insert into usuario (login,nome,senha,email) values (%s,%s,%s,%s)'
val = [
        ('joy', 'Joyce', '123', 'joyce@soulasalle.com.br'),
        ('new', 'Newton', '1234', 'newton@soulasalle.com.br'),
        ('th', 'Thiago', '12345', 'thiago@soulasalle.com.br'),
        ('lu', 'Luiz', '123456', 'luiz@soulasalle.com.br'),
        ('lc', 'Lucas', '12', 'lucas@soulasalle.com.br'),
         ]
cursor.executemany(sql,val)
conexao.commit()

cursor.execute('update usuario set senha = "1234567" where login="lc" ')
conexao.commit()

cursor.execute('delete from usuario where login="new"')
conexao.commit()
'''

cursor.execute('select * from usuario where login="th"')
result = cursor.fetchall()

i = Tk()

i.title('Prova AV2')

i.wm_iconbitmap('b.ico')

i.geometry('400x500')


def insere():
    f = a1.get()
    g = b2.get()
    h = c3.get()
    i = d4.get()
    try:
        if (f == '' or g == '' or h == '' or i == ''):
            MessageBox.showinfo('Status inserido', 'Todos os campos são obrigatórios.')
        else:
            con = mysql.connect(host='localhost', user='root', password='', database='provaav2')
            cursor = con.cursor()
            cursor.execute(
                "insert into usuario values(' " + f + " ', ' " + g + " ', ' " + h + " ', ' " + i + " ')")
            cursor.execute('commit')
            MessageBox.showinfo('Status inserido', 'Inserido com sucesso!')
            con.close()
    except:
        MessageBox.showinfo(title='Aviso',
                            message='Nick já existe.')


def busca():
    l = a1.get()
    try:
        con = mysql.connect(host='localhost', user='root', password='', database='provaav2')
        cursor = con.cursor()
        cursor.execute(
            "select login from usuario")
        dados = cursor.fetchall()

        for _ in dados:
            if l != ' ' and l in _:
                MessageBox.showinfo(title='Aviso', message='Busca realizada com sucesso!')
                break
            else:
                MessageBox.showinfo(title='Aviso',
                                    message='Usuário inexistente.')
                break
    except:
        MessageBox.showinfo(title='Aviso',
                            message='Usuário inexistente.')

def altera():
    f = c3.get()
    g = a1.get()
    cursor.execute('update usuario set senha = "'+ f +'," where login ="'+ g +'" ')
    conexao.commit()
    MessageBox.showinfo(title='Aviso', message='Alteração realizada com sucesso!')

def exclui():
    g = a1.get()
    cursor.execute('delete from usuario where login ="' + g + '" ')
    conexao.commit()
    MessageBox.showinfo(title='Aviso', message='Exclusão realizada com sucesso!')

a = Label(i,
          text='Informe os dados:',
          fg='black',
          font='oswald 15 bold',
          bg='lightblue',
          bd='2px'
          )

a.place(x=130, y=50)

b = Label(i,
          text='idUsuario:',
          fg='black',
          font='oswald 10 bold',
          bg='lightblue',
          bd='2px'
          )

b.place(x=100, y=100)

c = Label(i,
          text='Nome:',
          fg='black',
          font='oswald 10 bold',
          bg='lightblue',
          bd='2px'
          )

c.place(x=100, y=140)

d = Label(i,
          text='Senha:',
          fg='black',
          font='oswald 10 bold',
          bg='lightblue',
          bd='2px'
          )

d.place(x=100, y=180)

e = Label(i,
          text='Email:',
          fg='black',
          font='oswald 10 bold',
          bg='lightblue',
          bd='2px'
          )

e.place(x=100, y=220)

a1 = Entry()
a1.place(x=190, y=105)

b2 = Entry()
b2.place(x=190, y=145)

c3 = Entry(show='*')
c3.place(x=190, y=185)

d4 = Entry()
d4.place(x=190, y=225)

buscar = Button(i, text='Buscar', bd='2px', font='oswald 10 bold', command=busca)
buscar.place(x=320, y=100)

inserir = Button(i, text='Inserir', bd='2px', font='oswald 10 bold', command=insere)
inserir.place(x=90, y=300)

alterar = Button(i, text='Alterar', bd='2px', font='oswald 10 bold',command=altera)
alterar.place(x=160, y=300)

excluir = Button(i, text='Excluir', bd='2px', font='oswald 10 bold',command=exclui)
excluir.place(x=234, y=300)


i.mainloop()
