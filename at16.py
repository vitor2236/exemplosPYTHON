import math

def calcular_latas_galoes(area):
    litros_necessarios = area / 6 * 1.10  # Adiciona 10% de folga
    latas_18 = math.ceil(litros_necessarios / 18)
    litros_restantes = litros_necessarios % 18
    galoes_36 = math.ceil(litros_restantes / 3.6)
    return latas_18, galoes_36

def calcular_preco_total(latas_18, galoes_36):
    preco_lata = 80.00
    preco_galao = 25.00
    preco_total_latas = latas_18 * preco_lata
    preco_total_galoes = galoes_36 * preco_galao
    return preco_total_latas, preco_total_galoes

area_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

latas_18, galoes_36 = calcular_latas_galoes(area_pintada)
preco_total_latas, preco_total_galoes = calcular_preco_total(latas_18, galoes_36)

print(f"Quantidade de latas de 18 litros a serem compradas: {latas_18}")
print(f"Preço total das latas de 18 litros: R$ {preco_total_latas:.2f}")
print(f"Quantidade de galões de 3,6 litros a serem comprados: {galoes_36}")
print(f"Preço total dos galões de 3,6 litros: R$ {preco_total_galoes:.2f}")

# Verifica a melhor opção considerando a mistura de latas e galões
litros_mistura = latas_18 * 18 + galoes_36 * 3.6
latas_mistura = math.ceil(litros_mistura / 18)
preco_total_mistura = latas_mistura * 80.00
print(f"Melhor opção misturando latas e galões:")
print(f"Quantidade de latas: {latas_mistura}")
print(f"Preço total da mistura: R$ {preco_total_mistura:.2f}")