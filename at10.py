def calcular_produto_e_soma(numero1, numero2, numero_real):
    produto = (2 * numero1) * (numero2 / 2)
    soma = (3 * numero1) + numero_real
    cubo = numero_real ** 3
    return produto, soma, cubo

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite o número real: "))

produto, soma, cubo = calcular_produto_e_soma(numero1, numero2, numero_real)

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo:.2f}")