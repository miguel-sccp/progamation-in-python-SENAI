#1
def comparar_num():
                 num=5
                 if num%2==0:
                   print('numero é par ')
                 else:
                     print('numero é impar')

comparar_num()
#2
def mul_num(n1,n2,n3):
    print('=',(n1*n2)*n3)

mul_num(10,20,30)
#3
def  exponencia(n1,n2):
 print('=',n1**n2)
 
exponencia(3,2)

#4
def ida():
 ida=int(input('digite sua idade'))
 if ida== 18:
    print('vc pode chapar o coco')

ida()
#5
print('vou adivinhar sua idade')
def idade():
 n1=int(input('digite ano q nasceu'))
 n2=int(input('digite o ano atual'))
 print('sua idade é:', n2-n1)
idade()
#6
def copa():
    copa=[1958,1962,1970,1994,2022]
    ano=int(input('digite o ano que o brasil foi campeão do mundo'))
    if ano in copa:
        print('esse ano o brasil foi campeçãodo mundo')
    else:
        print('esse ano o brasil nao foi campeão')
copa()
print()
#7

def restaurante():
    lista =  ['','Macarronada', 'Salada', 'Sanduiche', 'Sorvete']
    print(lista)
    escolha  =  int(input('Digite o id do produto: '))
    print('Escolha: ',  lista[escolha])

while True:
      restaurante()

    
        





