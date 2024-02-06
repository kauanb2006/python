# Solicita o primeiro número
numero_anterior = int(input("Digite um número inteiro: "))

# Solicita números inteiros maiores que o anterior
while True:
    numero_atual = int(input("Digite outro número inteiro maior que o anterior (digite um número menor para encerrar): "))
    
    if numero_atual < numero_anterior:
        break
    else:
        numero_anterior = numero_atual

print("Programa encerrado.")
