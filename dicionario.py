contatos={}
for i in range(3):
   nome= input(f"digite o nome da pessoa{i+1}:")
   tel=input(f"digite o telefone da{nome}:")
   contatos[nome]=tel

print("Contatos")
for nome, tel in contatos.items():
     print(f"{nome}:{telefone}")















