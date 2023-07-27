def converter_para_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Digite a temperatura em graus fahrenhit: "))
celsius = converter_para_celsius(fahrenheit)
print(f"A temperatura em Celsius é: {celsius: .2f} ")