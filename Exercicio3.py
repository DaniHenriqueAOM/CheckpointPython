print("EXERCÍCIO 3\n")

idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print(f"\nA idade do nadador é de {idade} anos, logo ele fará parte da Categoria INFANTIL A!\n")
elif idade >= 8 and idade <= 10:
    print(f"\nA idade do nadador é de {idade} anos, logo ele fará parte da Categoria INFANTIL B!\n")
elif idade >= 11 and idade <= 13:
    print(f"\nA idade do nadador é de {idade} anos, logo ele fará parte da Categoria JUVENIL A!\n")
elif idade >= 14 and idade <= 17:
    print(f"\nA idade do nadador é de {idade} anos, logo ele fará parte da Categoria JUVENIL B!\n")
elif idade >= 18:
    print(f"\nA idade do nadador é de {idade} anos, logo ele fará parte da Categoria Sênior!\n")