# Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro para exibir a tabuada: "))

# Exibe a tabuada do número fornecido
print(f"Tabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
