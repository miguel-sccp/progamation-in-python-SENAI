# e-commerce com lista
produtos =['', 'iphone 17', 'notebook', 'fone', 'ssd']
valores=['', 7000.00,10000.00,400.7,350.55]

print('escolha o produto através do ID 1-2-3-4')
print('PRODUTOS DA LOJA X')
print(produtos[1],"R$",valores[1])
print(produtos[2],"R$",valores[2])
print(produtos[3],"R$",valores[3])
print(produtos[4],"R$",valores[4])

pedido1=int(input('digiteo id do produto'))
pedido2=int(input('digiteo id do produto'))
pedido3=int(input('digiteo id do produto'))
pedido4=int(input('digiteo id do produto'))



carrinho=[]
meu_total=[]

carrinho.append(produtos[pedido1])
carrinho.append(produtos[pedido2])
carrinho.append(produtos[pedido3])
carrinho.append(produtos[pedido4])



meu_total.append(valores [pedido1])
meu_total.append(valores [pedido2])
meu_total.append(valores [pedido3])
meu_total.append(valores [pedido4])
print('PRODUTOS NO CARRINHO',carrinho)
total=sum(meu_total)
print('R$', total)
print("escolha a forma de pagamento")

print('escolha a forma de pagamento 1 pix 3 cc 3 paypall')
formas=['','pix','cc','paypall']
escollha=int(input('difite o ID:'))
print('A sua forma de pagamento é', formas[escollha])
print('-----------------------x-----------------------')
print('obrigado volte sempre')
