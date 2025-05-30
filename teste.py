Dito por si:
print('seja bem vindo faça seu cadstrastro')
pessoas={}
for i in range(3):
   nome= input(f"digite o nome da pessoa {i+1}:")
   idade=input(f"digite o idade do(a):{nome}:")
   pessoas[nome]=idade
quartos_dispo=['','simples', 'duplo', 'luxo']
preco=['',100, 150, 250]
print(' escolha seu quarto através do Id 1-2-3-4')
print('qurtos disponiveis')
print(quartos_dispo[1],"R$/dia",preco[1])
print(quartos_dispo[2],"R$/dia",preco[2])
print(quartos_dispo[3],"R$/dia",preco[3])
pedido1=int(input('digiteo id do quarto'))
pedido2=int(input('digiteo id do quarto'))
pedido3=int(input('digiteo id do quarto'))
carrinho=[]
meu_total=[]

carrinho.append(quartos_dispo[pedido1])
carrinho.append(quartos_dispo[pedido2])
carrinho.append(quartos_dispo[pedido3])


meu_total.append(preco [pedido1])
meu_total.append(preco [pedido2])
meu_total.append(preco [pedido3])


dia_nome1=int(input('quantos dias a', nomes[1] ,'ira ficar?'))
dia_nome2=int(input('quantos dias a', nomes[2] ,'ira ficar?'))
dia_nome3=int(input('quantos dias a', nomes[3] ,'ira ficar?'))

print('o(a)',nomes[1], 'irá ficar',carrinho.append(quartos_dispo[pedido1])*dia_nome1, 'dias')
print('o(a)',nomes[2], 'irá ficar',carrinho.append(quartos_dispo[pedido2])*dia_nome1, 'dias')
print('o(a)',nomes[3], 'irá ficar',carrinho.append(quartos_dispo[pedido3])*dia_nome1, 'dias')


print('o(a)',nomes[1], 'irá ficar',carrinho.append(quartos_dispo[pedido1])*dia_nome1, 'dias')
print('o(a)',nomes[2], 'irá ficar',carrinho.append(quartos_dispo[pedido2])*dia_nome1, 'dias')
print('o(a)',nomes[3], 'irá ficar',carrinho.append(quartos_dispo[pedido3])*dia_nome1, 'dias')


