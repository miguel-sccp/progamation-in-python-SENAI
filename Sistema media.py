#siteam de media de notas


print("seja bem vindo(a) ao sistema de notas")

nome=input("digite o nome so aluno:")

nota_mat=float(input("digite a nota de matematica:"))

nota_por=float(input("digite a nota de portugues:"))

nota_ing=float(input("digite a nota de ingles:"))

media=(nota_mat+nota_por+nota_ing)/3

print("o aluno", nome, "esta com amedia", media)

aprovado= media>=6 
reprovado= media<5
recuperacão= media>=5 and media<6

print(f'''
O aluno{nome}
aprovado - {aprovado}
reprovadp - {reprovado}
recuperação - {recuperacão}
''')