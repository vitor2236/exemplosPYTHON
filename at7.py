def calcular_area_quadrado(lado):
 area = lado ** 2 
 return area

lado = float(input("Digite o valor do lado do quadrado: "))

area_quadrado = calcular_area_quadrado(lado)
dobro_area = 2 * area_quadrado

print(f"A área do quadrado é: {area_quadrado: .2f}")
print(f"O dobro da área do quadrado é: {dobro_area: .2f}")