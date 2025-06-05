

def soma(n1,n2):
    print('=',n1+n2)
def sub(n1,n2):
    print('=',n1-n2)
def mult(n1,n2):
    print('=',n1*n2)
def div(n1,n2):
    print('=',n1/n2)
def  exponencia(n1,n2):
    print('=',n1**n2)
def calculadora():
    n1=float(input(' =  '))
    op=input('escolha a operação + - * / ** ')
    if op=='+':
       n2=float(input( ' =  '))
       soma(n1,n2)
    elif op=='-':
        n2=float(input(' =  '))
        sub(n1,n2)
    elif op=='*':
        n2=float(input(' =  '))
        mult(n1,n2)
    elif op=='/':
        n2=float(input(' =  '))
        div(n1,n2)
    elif op=='**':
        n2=float(input(' =  '))
        exponencia(n1,n2)
 
        
    else:
     print('digite um operação valida burrão')

while True:
    calculadora()
input('digite enter para sair')

