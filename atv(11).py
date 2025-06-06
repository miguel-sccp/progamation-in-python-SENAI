import random

#1
def ale_num():
  ale = random.randint(5,10)
  print(ale)

ale_num()
#2
def num_ale():
    ale_1=random.randint(5,50)
    ale_2=random.randint(5,50)
    ale_3=random.randint(5,50)
    print(f'''
{ale_1}
{ale_2}
{ale_3}
     ''')
num_ale()
#3
def num_3_ale():
    ale_1=random.randrange(5,50)
    ale_2=random.randrange(5,50)
    ale_3=random.randrange(5,50)
    print(f'''
{ale_1}
{ale_2}
{ale_3}
     ''')
num_3_ale()
#4
def contagem_regressiva():
    for i in range(10,0,-1):
        print(i)
    print('fogo')


contagem_regressiva()
#5
def soma_pares():
    n=int(input('digite um num int'))
    I=[]
    for i in range(n):
      I.append(i)
      soma=sum(I)
    print(soma)
soma_pares()
#6
def taboada():
  n=int(input('digite o multiplicador da tabuada:'))
  for i in range(0,11):

    calculo= i*n
    print(n, 'x', i, '=', calculo)
taboada()
#7
def contagem_regressiva_impar():
    for i in range(99,0,-2):
        print(i)
    print('gelo')


contagem_regressiva_impar() 

