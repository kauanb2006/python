nome= input("Digite o nome do aluno: ")
trabalho = float(input("Digite a nota do trabalho: "))
while trabalho < 0 or prova1 >10:
    trabalho = float(input("Digite uma nota de 0 a 10: "))

prova1 = float(input("Digite a nota da prova 1: "))
while prova1 < 0 or prova1 >10:
    prova1 = float(input("Digite uma nota de 0 a 10: ")) 

prova2 = float(input("Digite a nota da prova 2: "))
while prova2 < 0 or prova1 >10:
    prova2 = float(input("Digite uma nota de 0 a 10: ")) 



    
  

media_final = trabalho * 0.3 + prova1  *0.35 + prova2* 0.35   
   
if media_final > 5.0:
    situacao = "Aprovado"
elif media_final > 3.5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Exibe os resultados na tela
print(f"Aluno: {nome}")
print(f"Média Final: {media_final:.2f}")
print(f"Situação: {situacao}")

