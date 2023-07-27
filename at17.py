def calcular_tempo_download(tamanho_arquivo, velocidade_internet):
    # Convertendo a velocidade para MB por segundo
    velocidade_mbps = velocidade_internet / 8
    # Calculando o tempo de download em segundos
    tempo_segundos = tamanho_arquivo / velocidade_mbps
    # Convertendo o tempo de segundos para minutos
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de internet (em Mbps): "))

tempo_minutos = calcular_tempo_download(tamanho_arquivo, velocidade_internet)

print(f"O tempo aproximado de download do arquivo é de {tempo_minutos:.2f} minutos.")