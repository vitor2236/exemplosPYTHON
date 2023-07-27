print("Digite as suas notas")

mat = float(input("Matemática: "))
port = float(input("Português: "))
fis = float(input("Física: "))
quim = float(input("Quimica: "))

resultado = (mat + port + fis + quim) // 4

print("Sua média é: ", resultado)