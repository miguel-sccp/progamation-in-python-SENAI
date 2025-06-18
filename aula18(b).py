from tkinter import *
from PIL import ImageTk, Image

def cadastrar():
    print('Cadastro de usuários')
    print(f'nome: , {nome.get()}')
    print(f'e-mail: , {email.get()}')
    print(f'celular: , {celular.get()}')

janela = Tk()
janela.configure(bg='black')
janela.title('Cadastro de usuários')
janela.geometry('450x500')
janela.resizable(False,False)

frame_principal = Frame(janela, padx =20, pady = 20)
frame_principal.pack(fill=BOTH, expand = True)
frame_principal.configure(bg='black')

try:
    img = Image.open('C:/Users/Aluno/auala 19/sccp.png')
    img = img.resize((150,150),Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)
    label_imagem = Label(frame_principal, image=tk_img)
    label_imagem.image = tk_img
    label_imagem.pack(pady = 10)
except:
    label_sem_imagem = Label(frame_principal, text = 'LOGO', font = ('arial',24))
    label_sem_imagem.pack(pady=20)


frame_form = Frame(frame_principal)
frame_form.pack(fill=BOTH, expand=True, pady=20)
frame_form.configure(bg='black')

Label(frame_form, text='nome: ', anchor='w',bg='black',fg='white').pack(fill=X, pady=(0,5))
nome = Entry(frame_form,bg='black', font=('arial', 12), fg='white')
nome.pack(fill=X, pady=(0,10))

Label(frame_form, text='e-mail: ', anchor='w',bg='black',fg='white').pack(fill=X, pady=(0,5))
email = Entry(frame_form,bg='black', font=('arial', 12), fg='white')
email.pack(fill=X, pady=(0,10))

Label(frame_form, text='celular: ', anchor='w',bg='black',fg='white').pack(fill=X, pady=(0,5))
celular = Entry(frame_form,bg='black', font=('arial', 12), fg='white')
celular.pack(fill=X, pady=(0,10))

btn   =  Button(frame_principal,text = 'CADASTRAR', command=cadastrar,
                bg = 'SlateBlue', fg = 'white', font=('arial', 12, 'bold'),
                padx=20,pady=10)

btn.pack()


Label(frame_principal, text='SISTEMA DE CADASTRO: ',fg= 'gray').pack(side=BOTTOM,pady=5)

janela.mainloop()
