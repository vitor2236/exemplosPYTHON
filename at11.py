def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

altura = float(input("Digite sua altura em metros: "))
peso_ideal = calcular_peso_ideal(altura)
print(f"Seu peso ideal é: {peso_ideal:.2f} kg")