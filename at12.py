def calcular_peso_ideal_homem(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

def calcular_peso_ideal_mulher(altura):
    peso_ideal = (62.1 * altura) - 44.7
    return peso_ideal


altura = float(input("Digite sua altura em metros: "))
genero = input("Digite 'H' para homem ou 'M' para mulher: ")

if genero.upper() == 'H':
    peso_ideal = calcular_peso_ideal_homem(altura)
elif genero.upper() == 'M':
    peso_ideal = calcular_peso_ideal_mulher(altura)
else:
    print("Opção inválida. Digite 'H' para homem ou 'M' para mulher.")


print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

