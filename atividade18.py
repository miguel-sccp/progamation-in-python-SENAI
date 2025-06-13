import tkinter as tk

def dispay():

    nome=nome_digitado.get()
    idade=idade_digitada.get()
    email=email_digitado.get()
    endereço=endereco_digitado.get()
    celular=celular_digitado.get() 
    Mostrar_nome.config(text=nome)
    Mostrar_idade.config(text=idade)
    Mostrar_email.config(text=email)
    Mostrar_endereco.config(text=endereço)  
    Mostrar_celular.config(text=celular)

    
janela= tk.Tk()
janela.title('SISTEMA DE CADASTRO')
janela.geometry('500x500')
titulo_pag = tk.Label(janela,text = 'Cadastro de usuários', font=('arial',15))
titulo_pag.grid(row=0,column=0, padx=15, pady=10)

Mostrar_nome= tk.Label(janela, text = 'NOME', font=('arial',10))
Mostrar_nome.grid(row=1, column=0, pady=5)
nome_digitado = tk.Entry(janela, font=('arial', 10))
nome_digitado.grid(row=1, column=1, padx=5, pady=5)

Mostrar_idade = tk.Label(janela, text = 'IDADE', font=('arial',10))
Mostrar_idade.grid(row=2, column=0, pady=5)
idade_digitada = tk.Entry(janela, font=('arial', 10))
idade_digitada.grid(row=2, column=1, padx=5, pady=5)

Mostrar_email = tk.Label(janela, text = 'EMAIL', font=('arial',10))
Mostrar_email.grid(row=3, column=0, pady=5)
email_digitado = tk.Entry(janela, font=('arial', 10))
email_digitado.grid(row=3, column=1, padx=5, pady=5)

Mostrar_endereco = tk.Label(janela, text = 'ENDEREÇO', font=('arial',10))
Mostrar_endereco.grid(row=4, column=0, pady=5)
endereco_digitado = tk.Entry(janela, font=('arial', 10))
endereco_digitado.grid(row=4, column=1, padx=5, pady=5)

Mostrar_celular = tk.Label(janela, text = 'CELULAR', font=('arial',10))
Mostrar_celular.grid(row=5, column=0, pady=5)   
celular_digitado = tk.Entry(janela, font=('arial', 10))
celular_digitado.grid(row=5, column=1, padx=5, pady=5)



botao = tk.Button(janela, text = 'eviar', font=('arial', 15), command=dispay)
botao.grid(row=6, column=0, padx=5, pady=5) 

Mostrar_nome = tk.Label(janela, text = '', font=('arial', 15))
Mostrar_nome.grid(row=7, column=0, padx=5, pady=5)

Mostrar_idade = tk.Label(janela, text = '', font=('arial', 15))
Mostrar_idade.grid(row=8, column=0, padx=5, pady=5)

Mostrar_email = tk.Label(janela, text = '', font=('arial', 15))
Mostrar_email.grid(row=9, column=0, padx=5, pady=5)

Mostrar_endereco = tk.Label(janela, text = '', font=('arial', 15))
Mostrar_endereco.grid(row=10, column=0, padx=5, pady=5)

Mostrar_celular = tk.Label(janela, text = '', font=('arial', 15))
Mostrar_celular.grid(row=11, column=0, padx=5, pady=5)



janela.mainloop()