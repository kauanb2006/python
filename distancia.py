origem = input	(" Cidade de origem :")
destino = input (" Cidade de destino :")
distancia = float (input("Qual a distancia em km ?"))
velocidade = float(input(" A quantos km/h irá viajar ?"))
tempo = distancia/velocidade*60
print (f" Você levará {tempo} minutos de {origem} à {destino}")