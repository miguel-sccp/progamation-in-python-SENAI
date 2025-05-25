print("seja bem vindo")
numero=[]
for i in range(5):
    valor=int(input(f"digite o {i+1}º numero"))
    numero.append(valor)

print("Lista:", numero)
print("Maior nuemro",max(numero))
print("menor nuemro",min(numero))
print("soma de todos os numeros",sum(numero))
print("qunatos numeors tem no total",len(numero))
