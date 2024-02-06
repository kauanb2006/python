
nome1 = input("Digite o nome do aluno 1: ")
nota1 = float (input("Digite o valor de 0-10 para a prova 1 :"))  
while nota1 < 0 or nota1 >10:
        nota1 = float(input("Digite uma nota de 0 a 10: ")) 

nome2 = input("Digite o nome do aluno 2: ")
nota2 = float(input("Digite a nota 2: ")) 
while nota2 < 0 or nota2 >10:
        nota2 = float(input("Digite uma nota de 0 a 10: ")) 


nome3 = input("Digite o nome do aluno 3: ")
nota3 =float(input("Digite a nota 3: ")) 
while nota3 < 0 or nota3 >10:
        nota3 = float(input("Digite uma nota de 0 a 10: ")) 

aluno =  None
maior = None

        
if  nota1> nota2 and nota1> nota3:
        maior = nota1
        aluno = nome1
print(f"O aluno{aluno}teve a maior nota{maior}.")


    
