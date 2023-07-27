def calcular_excesso_multa(peso):
    limite_peso = 50.0
    excesso = max(peso - limite_peso, 0)  # O excesso é zero se o peso não ultrapassar o limite
    multa = excesso * 4.0
    return excesso, multa

peso_peixes = float(input("Digite o peso de peixes (em quilos): "))

excesso, multa = calcular_excesso_multa(peso_peixes)

print(f"Você excedeu o limite de peso em {excesso:.2f} kg.")
print(f"A multa a ser paga é de R$ {multa:.2f}.")