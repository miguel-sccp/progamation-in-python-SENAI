import random

lista=['pedra','papel','tesoura']
escolha_computador=random.choice(lista)

escolha_usuario=input('digite sua opção')

if escolha_computador==escolha_usuario:
    print("EMPATE")
elif escolha_computador=='papel'and escolha_usuario=='pedra':
  print('O CPU GANHOU')
elif escolha_computador=='pedra'and escolha_usuario=='papel':
  print('vc ganhou')
elif escolha_computador=='papel'and escolha_usuario=='tesoura':
    print ('vc ganhou')
elif escolha_computador=='tesoura'and escolha_usuario=='papel':
    print ('cpu ganhou')
elif escolha_computador=='papel'and escolha_usuario=='tesoura':
    print ('vc ganhou')
elif escolha_computador=='tesoura'and escolha_usuario=='pedra':
    print('cpu ganhou')
elif escolha_computador=='pedra'and escolha_usuario=='tesoura':
    print('vc ganhou')

enter=input('digite enter para sair')

