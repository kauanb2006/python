j = input ("Você está em jejum s/n?")
t = input ("trigliceres? ")
t = int (t) # converter para int 
if j == 's': 
    if t > 150 :
        print("Está alto!")
    else:
        print("Está normal!")
else:
    if t > 175:
          print("Está alto!")
    else:
        print("Está normal!")