import random

chances=[3, 2, 1]

for i in chances:
    numero_ale=random.randint(1,2)
    chute=int(input('digite seu chute:'))
    print('vc tem apenas...',i, 'chances')
    if numero_ale==chute:
        print('acertou')
        break
    else:
        print('errou feio!')
else:
    print('chancse esgotada, game over')
