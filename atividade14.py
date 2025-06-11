#1
texto=''
match texto:
  case "":  # string vazia
     print('essa string é vazia')
  case _:   # qualquer outra coisa (não vazia)
     print('tem alguma coisa na string')
#2
n=10
match n:
   case n if n >10:
       print('e menor q 10')
   case n if n <10:
       print('e maior q 10')
   case 10:
       print('e igual q 10')
#3
idade=int(input('digite sua idade'))
match idade:
    case idade if idade==12:
        print('vc é criança')
    case idade if idade==17:
        print('vc é adolecente')
    case idade if idade==35:
        print('vc é joven')
    case idade if idade>65:
        print('vc é idoso')
    case idade if idade>35:
        print('vc é aulto')
    