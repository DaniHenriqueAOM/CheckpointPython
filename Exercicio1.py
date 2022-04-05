print("EXERCÍCIO 1\n")

nomev = input("Digite o Nome do Vendedor: ")
salaf = float(input("Digite o Salário Fixo: "))
vendas = float(input("Digite o Valor total de vendas efetuadas no mês (Em dinheiro): "))

com = vendas * (15/100)

total = com + salaf

print(f"O Nome do vendedor é: {nomev}\nEle recebe R${salaf} fixo por mês\nNesse mês ele vai receber de comissão R${com}\n Logo no final ele receberá R${total}!")