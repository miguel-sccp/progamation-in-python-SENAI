#e-commerce

carrinho=[]
m_valores=[]

comprar=input('deseja fzer pedido?: s/n')

produtos=['','a','b','c']
valor=['',100.0,200.0,300.0]
while comprar =='s':
    meu_prod= int(input(f'''
    Digite o ID 1 Produto A R${valor[1]}
    Digite o ID 2 produto B R${valor[2]}
    Digite o ID 3 produto C R${valor[3]}
    '''))
    carrinho.append(meu_prod)
    m_valores.append(valor[meu_prod])
    print('seus produtos', carrinho)
    soma=sum(m_valores)
    print('R$', soma)
    comprar =  input('Deseja continuar?: s/n ')
else:
    
    print('---'*10)
    print('R$', soma )
    print('escolha a forma de pagamento 1 pix 3 cc 3 paypall')
    formas=['','pix','cc','paypall']
    escollha=int(input('difite o ID:'))
    print('A sua forma de pagamento é', formas[escollha])
    print('-----------------------x-----------------------')
    print('obrigado volte sempre')
