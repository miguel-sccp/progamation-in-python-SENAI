#1

#a
n=0
while n<= 1000:
    print(n)
    n=n+1
#b
nomes=[]
for i in range(1,11):
 nome=input('digite seu nome')
 nomes.append(nome)
print(nomes)

#2
aluno='miguel'
senha= '9899'
listas_notas  = []

tentativa=0
while tentativa<=3:
    acesso=input('digite seu login')
    senha_acesso=input('digite sua senha')
    if acesso==aluno and senha_acesso==senha:
        quant_mat = int(input('Quantas notas'))
        for n in range(quant_mat):
            notas =float(input('Nota'))
            listas_notas.append(notas)

        media=sum(listas_notas)
        media=media/quant_mat
        print(media)
        break
    else:
        print('erro de digitação')
else:
    print('senha bloqueada')
    
