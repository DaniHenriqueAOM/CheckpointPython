print("EXERCÍCIO 2\n")

salariof = float(input("Digite o salário do funcionario: "))

if salariof > 0 and salariof < 1257.12:
    print("Esta isento de inposto.")
elif salariof >= 1257.12 and salariof < 2510.00:
    imposto = salariof * (17/100)
    sala_liq = salariof - imposto
elif salariof >= 2510.00:
    imposto = salariof * (28/100)
    sala_liq = salariof - imposto

print(f"\nSalário bruto: {salariof}\nSalário liquido: {sala_liq}\nValor do imposto: {imposto}\n")