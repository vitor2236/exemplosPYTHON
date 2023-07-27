def calcular_salario_mensal(valor_hora, horas_trabalhadas):
    salario_mensal = valor_hora * horas_trabalhadas
    return salario_mensal

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digit o número de horas trabalhadas no mês: "))

salario_total =calcular_salario_mensal(valor_hora, horas_trabalhadas)
print(f"O total do seu salário no mês é: R$ {salario_total: .2f}")