import math

def calcular_latas_tinta(area):
    litros_necessarios = area / 3
    latas_necessarias = math.ceil(litros_necessarios / 18)
    return latas_necessarias

def calcular_preco_total(latas_necessarias):
    preco_lata = 80.00
    preco_total = latas_necessarias * preco_lata
    return preco_total

area_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

latas_necessarias = calcular_latas_tinta(area_pintada)
preco_total = calcular_preco_total(latas_necessarias)

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total a pagar: R$ {preco_total:.2f}")